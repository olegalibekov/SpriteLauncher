def get_json_obj(obj_name, orig_tile_size, row_el_number, resolutions):
    json_data = {obj_name: {'highResolution': {}, 'mediumResolution': {},
                            'lowResolution': {}}}
    for resolution in resolutions:
        tile_size = orig_tile_size
        if resolution == 'mediumResolution':
            tile_size = {'width': orig_tile_size['width'] * resolutions['mediumResolution'],
                         'height': orig_tile_size['height'] * resolutions['mediumResolution']}
        if resolution == 'lowResolution':
            tile_size = {'width': orig_tile_size['width'] * resolutions['lowResolution'],
                         'height': orig_tile_size['height'] * resolutions['lowResolution']}

        tiles_position = []
        for tile_number in range(row_el_number):
            left_padding = tile_number * orig_tile_size['width'] * resolutions[resolution]
            if resolution == 'highResolution':
                tiles_position.append({'left': left_padding, 'top': 0.0})
            elif resolution == 'mediumResolution':
                tiles_position.append({'left': left_padding, 'top': float(orig_tile_size['height'])})
            elif resolution == 'lowResolution':
                tiles_position.append({'left': left_padding,
                                       'top': orig_tile_size['height'] + orig_tile_size['height'] *
                                              resolutions['mediumResolution']})

        data = {'tileSize': tile_size, 'tilesPosition': tiles_position}
        json_data[obj_name][resolution].update(data)
    return json_data
