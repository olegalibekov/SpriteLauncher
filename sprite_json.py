import json


def modify_json(json_data, obj_name, orig_tile_size, row_el_number, resolutions):
    json_data['spriteObjs'] = {obj_name: {'highResolution': {}, 'mediumResolution': {},
                                          'lowResolution': {}}}
    # json_data = json.dumps(json_data)
    for resolution in resolutions:
        tiles_position = []
        for tile_number in range(row_el_number):
            left_padding = tile_number * orig_tile_size['width'] * resolutions[resolution]
            if resolution == 'highResolution':
                tiles_position.append({'left': left_padding, 'top': 0})
            elif resolution == 'mediumResolution':
                tiles_position.append({'left': left_padding, 'top': orig_tile_size['height']})
            elif resolution == 'lowResolution':
                tiles_position.append({'left': left_padding,
                                       'top': orig_tile_size['height'] + orig_tile_size['height'] *
                                               resolutions['mediumResolution']})

        data = {'tileSize': orig_tile_size, 'tilesPosition': tiles_position}
        json_data['spriteObjs'][obj_name][resolution] = data
        json_data.update(json_data['spriteObjs'])
        # print(json_data)
    return json_data['spriteObjs']
