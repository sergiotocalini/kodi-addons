# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
VIDEOS = {
        'Season 03': [
             {'name': '03x01 - Papá Esta Loco',
              'thumb': 'https://3.bp.blogspot.com/-PWGlbmGHoWw/WlwoqFl05nI/AAAAAAABGZ8/eW9UYtWMV1k4qlTyS7M0hCebmNW5ntRCwCLcBGAs/s200/21.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/WGTWXkoOTnYARYCm3OEwkk6ZsHMcAa_Vc45cok8Go2seJxFPc',
              'genre': 'Bart deja su gorra roja en el lavarropas, por lo que todas las camisas de Homero se tiñen de rosa. Homero usa una de esas camisas rosas en la planta nuclear. Se lo toma por loco y se lo manda a un manicomio, donde conoce a un hombre que habla y camina como Michael Jackson. Estrella invitada: Michael Jackson (bajo el seudónimo de John Jay Smith).'
             },
         ],
         'Season 06': [
             {'name': '06x01 - El diabolico Bart',
              'thumb': 'https://2.bp.blogspot.com/-Ft0IXGgGWY0/Wn94spc-N7I/AAAAAAABG2Q/SLmlSyp5mRwqXdbh8f2bk6U8ozSneYNDwCLcBGAs/s200/21.jpg',
              'video': 'https://content-na.drive.amazonaws.com/cdproxy/templink/0H8U9kEQc9SMkRF-uVO6fFtJGNrLnADUPMhDZoZ3hAYeJxFPc',
              'genre': 'Los Simpsons compran una pileta y disfrutan de una inmediata popularidad. Pero Bart se rompe una pierna, y pasa el verano en la ventana de su pieza, mirando a los vecinos con un telescopio. Se aburre hasta que ve a Ned Flanders matar a su esposa.'
             },
             {'name': '06x02 - La rival de Lisa',
              'thumb': 'https://image.tmdb.org/t/p/original/gw2MG9ImULSND503EsOueuBV2dK.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/JxHJgBjKK4Usdvix6yrbRdDqcelEOZrmVmFknarZzHEeJxFPc',
              'genre': 'Una nueva compañera de Lisa es más inteligente, más joven y toca mejor el saxo que ella, situación que asusta a Lisa. Mientras, Homero encuentra un camión de azúcar volcado y empieza a vender azúcar. Estrella invitada: Winona Ryder.'
             },
             {'name': '06x03 - Recuerdos de amor',
              'thumb': 'https://image.tmdb.org/t/p/original/cfxlTb5adP02ihAXveNyUM4bnJl.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/_gXA1UH8kTw_-uQBTVKcB7Cy-zjKKOHf2HhFPQ6XqrUeJxFPc',
              'genre': 'Después de leer una novela romántica, Marge anima a la familia a recordar sus romances del pasado, lo que sirve como excusa para presentar fragmentos de episodios anteriores.'
             },
             {'name': '06x04 - La tierra de Tomy y Daly',
              'thumb': 'https://image.tmdb.org/t/p/original/5u7BWr0Q6rqm0MZAgp2dz0vFULs.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/bZ8tNIqlmS5wzo7zxGjRFrW9U1dRXf9lQYavMEmgPJEeJxFPc',
              'genre': 'El viaje familiar a la tierra de Tomy y Daly, el lugar más violento de la Tierra, es una carga hasta que todos los robots enloquecen y quieren asesinar a la familia.'
             },
             {'name': '06x05 - El regreso de Bob Patino',
              'thumb': 'https://image.tmdb.org/t/p/original/yBqxPRC19w6emH3RmQBTjkj4R9f.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyxtcrz3b4quuoawuqgikxlbqxxpoavd4fvtbbm4xc3umzod62ic3c/video.mp4',
              'genre': 'Con la ayuda de un locutor de radio, el alcalde Diamante es presionado para que libere a Bob Patiño. Cuando sale, Bob se postula para alcalde y gana. Ahora, Bart y Lisa deberán probar que no ganó legalmente. Estrellas invitadas: Dr.Demento, Larry King y Henry Corden.'
             },
             {'name': '06x06 - Especial de noche de brujas V',
              'thumb': 'https://image.tmdb.org/t/p/original/yc8Un69DCQz7Dk0u2kzjwO7V6Ay.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyrtcrz3b4quuoawurk2sdki33pexytjciqg6elq5fqbkmjhxf6u4r/video.mp4',
              'genre': 'El resplandor: La familia debe cuidar la mansión del Sr. Burns, para asegurarse que trabajen Burns decide cortar la televisión y llevarse la cerveza, lo que causa que Homero enloquezca. - El castigo del tiempo: Homero logra que la tostadora lo haga retroceder en el tiempo, pero al matar un mosquito todo el presente cambia. - La cafetería de las pesadillas: Cuando las aulas de detención están superpobladas y se recortan los presupuestos de la cafetería, Skinner encuentra una misma solución para los dos problemas. Estrella invitada: James Earl Jones.'
             },
             {'name': '06x07 - La novia de Bart',
              'thumb': 'https://image.tmdb.org/t/p/original/jDbgXfM1X0FCWCSCVi3ybAgRyoz.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyttcrz3b4quuoawuq6kccjijfb2iozdsu6cmqdm2eqmhahwtd7d3t/video.mp4',
              'genre': 'Bart se enamora de la hija del reverendo Alegría, quien roba el dinero de las limoznas de la iglesia y hace que todos lo culpen a él. Estrella invitada: Meryl Streep.'
             },
             {'name': '06x08 - Lisa y los deportes',
              'thumb': 'https://image.tmdb.org/t/p/original/z7Q9IPY8AKVYyQITmOfRxu9W61u.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyntcrz3b4quuoawur4zsmkjjluc4jzpnkxkhqxpdwgb35hj2cr6qz/video.mp4',
              'genre': 'Para aprobar gimnasia, Lisa forma parte de un equipo infantil de hockey y se convierte en la jugadora más valiosa del grupo siendo tan buena como Bart, lo que hace que los dos hermanos entren en competencia directa, tanto en la cancha como en casa.'
             },
             {'name': '06x09 - Homero el malo',
              'thumb': 'https://image.tmdb.org/t/p/original/qLRhq2VDBrGO1lvt1vpooPlxDV9.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyptcrz3b4quuoawurcjcojq5tskasdprgjeq5y7rh52mdc5mdciti/video.mp4',
              'genre': 'La vida de Homero se arruina cuando el simple acto de agarrar una golosina es malinterpretado como acoso sexual por la nueva niñera de la familia. Estrella invitada: Dennis Franz.'
             },
             {'name': '06x10 - El abuelo y la ineficiencia romantica',
              'thumb': 'https://image.tmdb.org/t/p/original/rCUbpL76QltEZ8ARfhglrKuKEZS.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyjtcrz3b4quuoawurii2nlnrvmpc7quvfwvpobkbv5rbotxyspvgx/video.mp4',
              'genre': 'El tónico del Abuelo salva la vida sexual de Homero y Marge, pero quiebra la relación entre padre e hijo. Mientras, Bart piensa que Springfield está invadida por ovnis.'
             },
             {'name': '06x11 - Miedo a volar',
              'thumb': 'https://image.tmdb.org/t/p/original/m4vWKriQpW9ZsbwRCVM0bAmd0Nv.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyltcrz3b4quuoawurwyyrcxnridyaczvcerfxyjalrogeazhu6vo3/video.mp4',
              'genre': 'Se revela el miedo a volar de Marge cuando Homero consigue un viaje a casi cualquier estado. Para vencerlo, Marge consulta una psicóloga. Estrellas invitadas: Anne Bancroft como la psicóloga y Ted Danson, Rhea Perlman, Woody Harrelson, John Ratzenberger y George Wendt interpretando sus personajes de la serie Cheers.'
             },
             {'name': '06x12 - Homero el grande',
              'thumb': 'https://image.tmdb.org/t/p/original/uXjEWSke130ffFpV2ztZHGyUNvo.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyftcrz3b4quuoawuuqocwiowzjkfbvapjwqgrtxwu6thu2oaugm7u/video.mp4',
              'genre': 'Homero se une a una sociedad secreta, en la que su grandeza es revelada, pero sólo después de destruir el pergamino sagrado. Estrella invitada: Patrick Stewart.'
             },
             {'name': '06x13 - Y con Maggie son tres',
              'thumb': 'https://image.tmdb.org/t/p/original/fFn7sYsCFn0Dup4rK5sv8s7wMRj.jpg',
              'video': 'https://www14.mp4upload.com:282/d/qwxyhtcrz3b4quuoawuq62szjtoujhnxsk3pqfdx5yflxhn2e4t74loi/video.mp4',
              'genre': 'Cuando Lisa se pregunta por qué no hay fotos de Maggie en el álbum familiar, Homero le cuenta la historia de cómo tuvo que dejar su trabajo soñado cuando Maggie nació.'
             },
             {'name': '06x14 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x15 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x16 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x17 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x18 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x19 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x20 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x21 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x22 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x23 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x24 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },
             {'name': '06x25 - ',
              'thumb': '',
              'video': '',
              'genre': ''
             },

         ],
}


def get_url(**kwargs):
    """
    Create a URL for calling the plugin recursively from the given set of keyword arguments.

    :param kwargs: "argument=value" pairs
    :type kwargs: dict
    :return: plugin call URL
    :rtype: str
    """
    return '{0}?{1}'.format(_url, urlencode(kwargs))


def get_categories():
    """
    Get the list of video categories.

    Here you can insert some parsing code that retrieves
    the list of video categories (e.g. 'Movies', 'TV-shows', 'Documentaries' etc.)
    from some site or server.

    .. note:: Consider using `generator functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :return: The list of video categories
    :rtype: list
    """
    return VIDEOS.keys()


def get_videos(category):
    """
    Get the list of videofiles/streams.

    Here you can insert some parsing code that retrieves
    the list of video streams in the given category from some site or server.

    .. note:: Consider using `generators functions <https://wiki.python.org/moin/Generators>`_
        instead of returning lists.

    :param category: Category name
    :type category: str
    :return: the list of videos in the category
    :rtype: list
    """
    return VIDEOS[category]


def list_categories():
    """
    Create the list of video categories in the Kodi interface.
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, 'My Video Collection')
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get video categories
    categories = get_categories()
    # Iterate through categories
    for category in categories:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=category)
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': VIDEOS[category][0]['thumb'],
                          'icon': VIDEOS[category][0]['thumb'],
                          'fanart': VIDEOS[category][0]['thumb']})
        # Set additional info for the list item.
        # Here we use a category name for both properties for for simplicity's sake.
        # setInfo allows to set various information for an item.
        # For available properties see the following link:
        # http://mirrors.xbmc.org/docs/python-docs/15.x-isengard/xbmcgui.html#ListItem-setInfo
        list_item.setInfo('video', {'title': category, 'genre': category})
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=listing&category=Animals
        url = get_url(action='listing', category=category)
        # is_folder = True means that this item opens a sub-list of lower level items.
        is_folder = True
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def list_videos(category):
    """
    Create the list of playable videos in the Kodi interface.

    :param category: Category name
    :type category: str
    """
    # Set plugin category. It is displayed in some skins as the name
    # of the current section.
    xbmcplugin.setPluginCategory(_handle, category)
    # Set plugin content. It allows Kodi to select appropriate views
    # for this type of content.
    xbmcplugin.setContent(_handle, 'videos')
    # Get the list of videos in the category.
    videos = get_videos(category)
    # Iterate through videos.
    for video in videos:
        # Create a list item with a text label and a thumbnail image.
        list_item = xbmcgui.ListItem(label=video['name'])
        # Set additional info for the list item.
        list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
        # Set graphics (thumbnail, fanart, banner, poster, landscape etc.) for the list item.
        # Here we use the same image for all items for simplicity's sake.
        # In a real-life plugin you need to set each image accordingly.
        list_item.setArt({'thumb': video['thumb'], 'icon': video['thumb'], 'fanart': video['thumb']})
        # Set 'IsPlayable' property to 'true'.
        # This is mandatory for playable items!
        list_item.setProperty('IsPlayable', 'true')
        # Create a URL for a plugin recursive call.
        # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/wp-content/uploads/2017/04/crab.mp4
        url = get_url(action='play', video=video['video'])
        # Add the list item to a virtual Kodi folder.
        # is_folder = False means that this item won't open any sub-list.
        is_folder = False
        # Add our item to the Kodi virtual folder listing.
        xbmcplugin.addDirectoryItem(_handle, url, list_item, is_folder)
    # Add a sort method for the virtual folder items (alphabetically, ignore articles)
    xbmcplugin.addSortMethod(_handle, xbmcplugin.SORT_METHOD_LABEL_IGNORE_THE)
    # Finish creating a virtual folder.
    xbmcplugin.endOfDirectory(_handle)


def play_video(path):
    """
    Play a video by the provided path.

    :param path: Fully-qualified video URL
    :type path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


def router(paramstring):
    """
    Router function that calls other functions
    depending on the provided paramstring

    :param paramstring: URL encoded plugin paramstring
    :type paramstring: str
    """
    # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        if params['action'] == 'listing':
            # Display the list of videos in a provided category.
            list_videos(params['category'])
        elif params['action'] == 'play':
            # Play a video from a provided URL.
            play_video(params['video'])
        else:
            # If the provided paramstring does not contain a supported action
            # we raise an exception. This helps to catch coding errors,
            # e.g. typos in action names.
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of video categories
        list_categories()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
