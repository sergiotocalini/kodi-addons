# -*- coding: utf-8 -*-
# Module: default
# Author: Roman V. M.
# Created on: 28.11.2014
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html

import sys
from urllib import urlencode
from urlparse import parse_qsl
import xbmc, xbmcgui, xbmcaddon, xbmcplugin
import urlresolver

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

# Free sample videos are provided by www.vidsplay.com
# Here we use a fixed set of properties simply for demonstrating purposes
# In a "real life" plugin you will need to get info and links to video files/streams
# from some web-site or online service.
FANART = {
    'Season 06': 'https://upload.wikimedia.org/wikipedia/en/d/df/The_Simpsons_-_The_Complete_6th_Season.jpg',
}
VIDEOS = {
        'Season 03': [
             {'name': '03x01 - Stark Raving Dad',
              'thumb': 'https://image.tmdb.org/t/p/original/4FF7LnpvqQQKgixMoluxtcqAnEr.jpg',
              'video': 'https://openload.co/embed/3GM8BNfH1sA',
              'genre': "Mistakenly committed to a mental hospital, Homer meets a tall, stocky white man who claims to be Michael Jackson.",
             },
         ],
         'Season 06': [
             {'name': "06x01 - Bart of Darkness",
              'thumb': 'https://image.tmdb.org/t/p/original/rz9uFKuZLHz0UhtOf4SgnSir1xD.jpg',
              'video': 'https://content-na.drive.amazonaws.com/cdproxy/templink/0H8U9kEQc9SMkRF-uVO6fFtJGNrLnADUPMhDZoZ3hAYeJxFPc',
              'genre': "Stuck in his room with a broken leg, Bart hears a high-pitched scream. When he looks through his telescope, he sees a guilty Ned Flanders burying the evidence.",
             },
             {'name': "06x02 - Lisa's Rival",
              'thumb': 'https://image.tmdb.org/t/p/original/gw2MG9ImULSND503EsOueuBV2dK.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/JxHJgBjKK4Usdvix6yrbRdDqcelEOZrmVmFknarZzHEeJxFPc',
              'genre': "Lisa feels threatened when a new girl moves to Springfield: Allison is smart, pretty, a great saxophone player and a crack diorama builder. Lisa tries to befriend her new rival, but she's consumed with envy and competitiveness.",
             },
             {'name': '06x03 - Another Simpsons Clip Show',
              'thumb': 'https://image.tmdb.org/t/p/original/cfxlTb5adP02ihAXveNyUM4bnJl.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/_gXA1UH8kTw_-uQBTVKcB7Cy-zjKKOHf2HhFPQ6XqrUeJxFPc',
              'genre': "After reading the weepy best-seller The Bridges of Madison County, Marge sits down with the family and recalls romantic moments, along with temptations from her bowling instructor Jacques and Homer's coworker Mindy.",
             },
             {'name': '06x04 - Itchy & Scratchy Land',
              'thumb': 'https://image.tmdb.org/t/p/original/5u7BWr0Q6rqm0MZAgp2dz0vFULs.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/bZ8tNIqlmS5wzo7zxGjRFrW9U1dRXf9lQYavMEmgPJEeJxFPc',
              'genre': "The family's trip to Itchy & Scratchy Land takes an unexpected turn when high-tech robots malfunction and become violent.",
             },
             {'name': '06x05 - Sideshow Bob Roberts',
              'thumb': 'https://image.tmdb.org/t/p/original/yBqxPRC19w6emH3RmQBTjkj4R9f.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/njXtv-pZ2xTvr3a0OHaX5Rwcy1K4r0aGDXr3nH_fz_keJxFPc',
              'genre': "Backed by a cabal of Republicans and the talk radio blowhard Birch Barlow, Sideshow Bob runs for mayor of Springfield. When new mayor Bob decides to build a freeway right through the Simpson's' home, Bart and Lisa set out to prove the election was rigged.",
             },
             {'name': '06x06 - Treehouse of Horror V',
              'thumb': 'https://image.tmdb.org/t/p/original/yc8Un69DCQz7Dk0u2kzjwO7V6Ay.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/YtnyvwsIJmgr26MWR0-NvbRwC87v5vmt5EBa9xRi1e4eJxFPc',
              'genre': "In \"The Shinning,\" Homer becomes groundskeeper of Mr. Burns' isolated mountain mansion. Next, in \"Time and Punishment,\" Homer tries to fix the toaster and winds up traveling through time. In \"Nightmare Cafeteria,\" Principal Skinner finds an ingenious way to reduce overcrowding in the detention room and deal with cafeteria budget cuts.",
             },
             {'name': "06x07 - Bart's Girlfriend",
              'thumb': 'https://image.tmdb.org/t/p/original/jDbgXfM1X0FCWCSCVi3ybAgRyoz.jpg',
              'video': 'https://content-eu.drive.amazonaws.com/cdproxy/templink/vQaMBfILcQ5OjFtdqaQx5iHduWqu_o4YukGY7cZh9CweJxFPc',
              'genre': "Smitten with Reverend Lovejoy's daughter Jessica, Bart tries to reform to win her heart -- but what she really wants is a bad boy. When she steals the church collection plate, Bart finds he's in over his head.",
              },
             {'name': '06x08 - Lisa on Ice',
              'thumb': 'https://image.tmdb.org/t/p/original/z7Q9IPY8AKVYyQITmOfRxu9W61u.jpg',
              'video': 'https://rapidvideo.com/e/FMEA7V5F20', #'https://openload.co/embed/yqf8b2V8Ssk',
              'genre': "When she nearly flunks gym class, Lisa is forced to take up a sport. She's a natural at hockey, but things get complicated when her team faces off against Bart's. In a tense moment on the ice, sibling rivalry melts into sibling loyalty.",
             },
             {'name': '06x09 - Homer Badman',
              'thumb': 'https://image.tmdb.org/t/p/original/qLRhq2VDBrGO1lvt1vpooPlxDV9.jpg',
              'video': 'https://rapidvideo.com/e/FMEA7UGXQZ',
              'genre': "When Homer gropes for a gummy candy stuck to the babysitter's pants, she mistakes his intentions and turns the town against him.",
             },
             {'name': '06x10 - Grampa vs. Sexual Inadequacy',
              'thumb': 'https://image.tmdb.org/t/p/original/rCUbpL76QltEZ8ARfhglrKuKEZS.jpg',
              'video': 'https://rapidvideo.com/e/FMEA7VM9XN',
              'genre': "Grandpa Simpson's miracle elixir reinvigorates Homer and Marge's sex life. When father and son embark on an old-fashioned medicine show to sell the love tonic, they rake in the money, but eventually old resentments bubble up between them.",
             },
             {'name': '06x11 - Fear of Flying',
              'thumb': 'https://image.tmdb.org/t/p/original/m4vWKriQpW9ZsbwRCVM0bAmd0Nv.jpg',
              'video': 'https://openload.co/embed/1x0p5DeprbE',
              'genre': "When they try to go on vacation, the family discovers Marge's debilitating fear of flying. Marge consults a psychoanalyst to find the source of her baffling fear.",
             },
             {'name': '06x12 - Homer the Great',
              'thumb': 'https://image.tmdb.org/t/p/original/uXjEWSke130ffFpV2ztZHGyUNvo.jpg',
              'video': 'https://rapidvideo.com/e/FMEA93N12M',
              'genre': "Homer joins the secret society of the Stonecutters and is suddenly exalted when the brethren discover his birthmark. The ancient order is shaken to the core by the ineptitude of its new Chosen One.",
             },
             {'name': '06x13 - And Maggie Makes Three',
              'thumb': 'https://image.tmdb.org/t/p/original/fFn7sYsCFn0Dup4rK5sv8s7wMRj.jpg',
              'video': 'https://rapidvideo.com/e/FMEA8VQ0I0',
              'genre': "The story of Maggie's birth is told in flashbacks: after Homer quits the Springfield Nuclear Power Plant to pursue his dream of working at a bowling alley, Marge reveals that she is pregnant.",
             },
             {'name': "06x14 - Bart's Comet",
              'thumb': 'https://image.tmdb.org/t/p/original/eKWhgogf11Gh0ArjyaWX6Xpj06V.jpg',
              'video': 'https://openload.co/embed/MBqnJSERK2Q',
              'genre': "When Bart is forced to assist Principal Skinner in early-morning astronomy observations, he discovers a giant comet heading towards Springfield. Facing impending doom, the entire town shows up at the Flanders family bomb shelter.",
             },
             {'name': '06x15 - Homie the Clown',
              'thumb': 'https://image.tmdb.org/t/p/original/ncHTJ7mrOM0HLhaqBTthmZkpaco.jpg',
              'video': 'https://openload.co/embed/RXPDGVhV2kg',
              'genre': "Krusty the Clown's reckless spending forces him to open a clown college to keep afloat. New graduate Homer discovers the perks and perils of being Krusty.",
             },
             {'name': '06x16 - Bart vs. Australia',
              'thumb': 'https://image.tmdb.org/t/p/original/vEnIfyA9iKWe6FLunqGiq2ifS5U.jpg',
              'video': 'https://openload.co/embed/v_xmHJNdUbc',
              'genre': "After Bart's prank phone call to Australia goes awry, the Simpsons must fly out to the land down under and apologize to the Australian people. When they discover Bart's penalty will be a kick in the pants, international relations deteriorate.",
             },
             {'name': '06x17 - Homer vs. Patty and Selma',
              'thumb': 'https://image.tmdb.org/t/p/original/wAzgGSFbBHhGloBQIto5pmeqFHt.jpg',
              'video': 'https://openload.co/embed/kO3CLo-h-u4',
              'genre': "Homer must turn to his sisters-in-law for a loan. Relishing Homer's degradation, Patty and Selma make him their slave. But when the sisters are caught smoking on the job, Homer reluctantly covers for them, saving their jobs. Meanwhile, Bart is late to sign up for a gym class and must take the only class still open -- ballet.",
             },
             {'name': '06x18 - A Star Is Burns',
              'thumb': 'https://image.tmdb.org/t/p/original/7o3UHlzqOtf0mnBVxJXSiuPxXvQ.jpg',
              'video': 'https://openload.co/embed/64CGn2ZTG5g',
              'genre': "Springfield plays host to a film festival. Among the contenders for best film: Barney presents \"Pukahontas,\" a haunting meditation on his alcoholism; Mr. Burns commissions the fawning biography \"A Burns for All Seasons\"; and Hans Moleman exploits misfortune with \"Man Getting Hit by Football.\"",
             },
             {'name': "06x19 - Lisa's Wedding",
              'thumb': 'https://image.tmdb.org/t/p/original/4Bfoju6VSkw5MAEXyzZTNL8IYLu.jpg',
              'video': 'https://openload.co/embed/SlN7hAUI_Tc',
              'genre': "A fortune teller foresees Lisa's future marriage to an upper-crust Harvard classmate. After a series of embarrassing incidents, Lisa comes to realize that even though her family may not be classy, she loves them the way they are.",
             },
             {'name': '06x20 - Two Dozen and One Greyhounds',
              'thumb': 'https://image.tmdb.org/t/p/original/fO59TWwbA2KUnsMAJPNMvuHPypT.jpg',
              'video': 'https://openload.co/embed/A5pq2BjPs9o',
              'genre': "When Santa's Little Helper sires a litter of puppies, Mr. Burns adopts them, secretly scheming to use their pelts to make a fur tuxedo. When Bart and Lisa confront Mr. Burns, he relents and turns the puppies into racing dogs instead.",
             },
             {'name': '06x21 - The PTA Disbands',
              'thumb': 'https://image.tmdb.org/t/p/original/sewHQkn73PnzWFmPH3NGtrrHX5b.jpg',
              'video': 'https://openload.co/embed/RIfu6vU1HJE',
              'genre': "A teachers' strike forces the Board of Education to enlist PTA members as substitute teachers. Realizing he preferred the old regime, Bart locks Skinner and Mrs. Krabappel in a room together until they can agree on the contract.",
             },
             {'name': '06x22 - Round Springfield',
              'thumb': 'https://image.tmdb.org/t/p/original/enkDNomoUp03x8gfP85nDSz8HDE.jpg',
              'video': 'https://openload.co/embed/s2rFYPaB5Mo',
              'genre': "Lisa is reunited with her idol, Bleeding Gums Murphy, but their time together is short-lived. When the jazz legend passes away, a heartbroken Lisa wants to buy his rare album for $500 and play it on the local jazz station as a tribute.",
             },
             {'name': '06x23 - The Springfield Connection',
              'thumb': 'https://image.tmdb.org/t/p/original/m8f0vTLpypTuwN74oHJKZN7E1Tg.jpg',
              'video': 'https://openload.co/embed/uhM2hN9j06U',
              'genre': "After Marge helps catch a petty criminal, the adrenaline rush inspires her to join the Springfield Police Department. Marge experiences feelings of power and authority that she's never known before, but police corruption makes her question her newfound calling.",
             },
             {'name': '06x24 - Lemon of Troy',
              'thumb': 'https://image.tmdb.org/t/p/original/7gqTkgajON7aKu3OxWVCdhTSVuI.jpg',
              'video': 'https://openload.co/embed/CT0INPtdO2I',
              'genre': "The simmering rivalry between Springfield and a neighboring town heats up when Shelbyville kids steal Springfield's prized lemon tree.",
             },
             {'name': '06x25 - Who Shot Mr. Burns? (1)',
              'thumb': 'https://image.tmdb.org/t/p/original/ovlPZwOur2hQPJj60qlq1YUenPs.jpg',
              'video': 'https://openload.co/embed/cuAsO68pHSM',
              'genre': "In Part I of this two-part suspense story, Mr. Burns' evil schemes go too far. When Burns winds up shot, everyone is a suspect.",
             },

         ],
        'Season 07': [
             {'name': '07x01 - Who Shot Mr. Burns? (2)',
              'thumb': 'https://image.tmdb.org/t/p/original/dQp66ZkXbQE8VUduiVEyeBd61',
              'video': 'https://openload.co/embed/ofTMC8EjT0Q',
              'genre': "With Mr. Burns shot, Chief Wiggum investigates the crime, and nearly everyone in town has a motive. At the end, it all comes down to the Simpson DNA.",
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


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

def resolve_url(url):
    duration=7500   #in milliseconds
    message = "Cannot Play URL"
    stream_url = urlresolver.HostedMediaFile(url=url).resolve()
    # If urlresolver returns false then the video url was not resolved.
    if not stream_url:
        dialog = xbmcgui.Dialog()
        dialog.notification("URL Resolver Error", message, xbmcgui.NOTIFICATION_INFO, duration)
        return False
    else:        
        return stream_url    

def play_video2(path):
    """
    Play a video by the provided path.
    :param path: str
    """
    # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    vid_url = play_item.getfilename()
    stream_url = resolve_url(vid_url)
    if stream_url:
        play_item.setPath(stream_url)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(_handle, True, listitem=play_item)


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
            play_video2(params['video'])
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
