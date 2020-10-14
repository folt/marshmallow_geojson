import ujson
from marshmallow_geojson import GeoJSONSchema

geojson_schema = GeoJSONSchema()

# ==============================================================================
# geojson = {
#     'type': 'Point',
#     'coordinates': [-105.01621, 39.57422]
# }
#
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# print(geojson_schema.dumps(geojson))
# ==============================================================================
# geojson = {
#     "type": "MultiPoint",
#     "coordinates": [
#         [-105.01621, 39.57422],
#         [-80.666513, 35.053994]
#     ]
# }
#
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
# geojson = {
#     "type": "LineString",
#     "coordinates": [
#         [-99.113159, 38.869651],
#         [-99.0802, 38.85682],
#         [-98.822021, 38.85682],
#         [-98.448486, 38.848264]
#     ]
# }
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
# geojson = {
#     "type": "MultiLineString",
#     "coordinates": [
#         [
#             [-105.019898, 39.574997],
#             [-105.019598, 39.574898],
#             [-105.019061, 39.574782]
#         ],
#         [
#             [-105.017173, 39.574402],
#             [-105.01698, 39.574385],
#             [-105.016636, 39.574385],
#             [-105.016508, 39.574402],
#             [-105.01595, 39.57427]
#         ],
#         [
#             [-105.014276, 39.573972],
#             [-105.014126, 39.574038],
#             [-105.013825, 39.57417],
#             [-105.01331, 39.574452]
#         ]
#     ]
# }
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
# geojson = {
#   "type": "Polygon",
#   "coordinates": [
#       [
#           [100, 0],
#           [101, 0],
#           [101, 1],
#           [100, 1],
#           [100, 0]
#       ]
#   ]
# }
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
# geojson = {
#     "type": "MultiPolygon",
#     "coordinates": [
#         [
#             [
#                 [107, 7],
#                 [108, 7],
#                 [108, 8],
#                 [107, 8],
#                 [107, 7]
#             ]
#         ],
#         [
#             [
#                 [100, 0],
#                 [101, 0],
#                 [101, 1],
#                 [100, 1],
#                 [100, 0]
#             ]
#         ]
#     ]
# }
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
# geojson = {
#     "type": "GeometryCollection",
#     "geometries": [
#         {
#             "type": "Point",
#             "coordinates": [-80.660805, 35.049392]
#         },
#         {
#             "type": "Polygon",
#             "coordinates": [
#                 [
#                     [-80.664582, 35.044965],
#                     [-80.663874, 35.04428],
#                     [-80.662586, 35.04558],
#                     [-80.663444, 35.046036],
#                     [-80.664582, 35.044965]
#                 ]
#             ]
#         },
#         {
#             "type": "LineString",
#             "coordinates": [
#                 [-80.662372, 35.059509],
#                 [-80.662693, 35.059263],
#                 [-80.662844, 35.05893]
#             ]
#         }
#     ]
# }
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
# geojson = {
#     "type": "Feature",
#     "geometry": {
#         "type": "Polygon",
#         "coordinates": [
#             [
#                 [-80.724878, 35.265454],
#                 [-80.722646, 35.260338],
#                 [-80.720329, 35.260618],
#                 [-80.71681, 35.255361],
#                 [-80.704793, 35.268397],
#                 [-82.715179, 35.267696],
#                 [-80.721359, 35.267276],
#                 [-80.724878, 35.265454]
#             ]
#         ]
#     },
#     "properties": {}
# }
# geojson_text = ujson.dumps(geojson)
# print(geojson_schema.loads(geojson_text))
# ==============================================================================
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [-80.870885, 35.215151]
            },
            "properties": {}
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-80.724878, 35.265454],
                        [-80.722646, 35.260338],
                        [-80.720329, 35.260618],
                        [-80.704793, 35.268397],
                        [-80.724878, 35.265454]
                    ]
                ]
            },
            "properties": {}
        }
    ]
}
geojson_text = ujson.dumps(geojson)
print(geojson_schema.loads(geojson_text))
