import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics.pairwise import euclidean_distances


class Figure:

    def __init__(self, array, wells, filter):
        self.array = array
        self.wells = wells
        self.filter = filter

        df = pd.DataFrame(self.array)
        ax = df.plot(kind='scatter', x='x', y='y')
        df[['x', 'y', 'name']].apply(lambda row: ax.text(*row), axis=1)
        distance = pd.DataFrame(euclidean_distances(df[['x', 'y']]))
        well_names = df['name']
        distance.columns = well_names
        self.df_distance = pd.concat([df.drop(['x', 'y'], axis=1), distance], axis=1)

        self.df_train = self.df_distance.drop(self.wells, axis=0)
        self.df_test = self.df_distance.loc[self.wells]
        self.x = self.df_train.drop(['name', 'wct', 'id', 'bottom_perf', 'top_perf', 'st', 'in_prod', 'station_id_id'],
                                    axis=1)
        self.y = self.df_train['wct']
        self.x_test = self.df_test.drop(
            ['name', 'wct', 'id', 'bottom_perf', 'top_perf', 'st', 'in_prod', 'station_id_id'], axis=1)
        self.model = RandomForestRegressor(random_state=42, max_depth=None)
        self.model.fit(self.x, self.y)
        self.y_pred_train = self.model.predict(self.x)
        self.y_pred = self.model.predict(self.x_test)

    def fig__bar(self):
        self.model.feature_importances_
        feature_importances = pd.DataFrame()
        feature_importances['feature_name'] = self.x.columns.tolist()
        feature_importances['importance'] = self.model.feature_importances_
        feature_importances = feature_importances.sort_values(by='importance', ascending=False)

        fig__bar = px.bar(feature_importances,
                          x=feature_importances['importance'],
                          y=feature_importances['feature_name'],
                          title="Список важности признаков в порядке убывания",
                          width=1000, height=700)
        fig__bar.update_layout(yaxis={'categoryorder': 'total ascending'})

        return fig__bar

    def fig__scatter(self):
        fig__scatter = px.scatter(x=self.y_pred_train, y=self.y, labels={
            "x": "Дата",
            "y": "Обводненность"
        },
                                  title="Чем дальше скважина от красной линии - тем хуже она предсказана",
                                  text=self.df_train['name'], width=850, height=800)
        fig__scatter.add_trace(go.Scatter(x=[0, 100], y=[0, 100], mode='lines', name='',
                                          line=dict(color='red', width=1, dash='dash')))

        return fig__scatter

    def predict(self):
        return pd.DataFrame({'Имя скважины': self.df_test['name'],
                             'Прогноз обводнённости, %': self.y_pred.round(1)}).filter(items=self.filter, axis=0)

    def predict_list(self):
        return pd.DataFrame({'Имя скважины': self.df_train['name'],
                             'Прогноз обводнённости, %': self.y_pred_train.round(1),
                             'Текушая обводнённость, %': self.y.round(1),
                             'Разница': (self.y_pred_train - self.y).round(1)}).filter(items=self.filter, axis=0)

    def percent(self):
        return round(sum(abs(self.y_pred_train - self.y)) / len(self.y), 1)
