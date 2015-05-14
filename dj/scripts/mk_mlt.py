# mk_mlt.py 
# Makes a .mlt file
# uses template.mlt which was created using ShotCut GUI NLE


import xml.etree.ElementTree
import copy

import pprint


def mk_mlt(template, output, params):

    def set_text(node,prop_name,value=None):
        print(node_id,prop_name,value)
        p = node.find("property[@name='{}']".format(prop_name))
        if value is None:
            node.remove(p)
        else:
            p.text = value

    # parse the template 
    tree=xml.etree.ElementTree.parse(template)

    # grab nodes we are going to store values into
    nodes={}
    for id in [
        'pl_title_img', 'tl_title',
        'pl_foot_img', 'tl_foot',
        'pl_vid0', 'tl_vid1',
        'audio_fade_in', 'audio_fade_out',
        'title_fade','foot_fade',
        ]:

        node = tree.find(".//*[@id='{}']".format(id))
        # import code; code.interact(local=locals())
        nodes[id] = node

    # remove placeholder nodes
    mlt = tree.find('.')
    play_list = tree.find("./playlist[@id='main bin']")
    nodes['pe'] = play_list.find("./entry[@sample]")
    for pe in play_list.findall("./entry[@sample]"):
        producer = pe.get('producer')
        producer_node = tree.find("./producer[@id='{}']".format(producer))
        print( producer )
        play_list.remove(pe)
        mlt.remove(producer_node)


    # add each clip to the playlist
    for clip in params['clips']:

        node_id = "pl_vid{}".format(clip['id'])

        pe = copy.deepcopy( nodes['pe'] )
        pe.set("producer", node_id)
        del pe.attrib["in"]
        del pe.attrib["out"]
        # set_text(pe,'length')
        play_list.insert(0,pe)

        pi = copy.deepcopy( nodes['pl_vid0'] )
        pi.set("id", node_id)
        del pi.attrib["in"]
        del pi.attrib["out"]
        # set_text(pi,'length')
        mlt.insert(0,pi)

        set_text(pi,'resource',clip['filename'])

    print("checking...")

    for pe in play_list.findall("./entry[@sample]"):
        producer = pe.get('producer')
        print(producer)

    # set title screen image
    set_text(nodes['pl_title_img'],'resource',params['title_img'])
    set_text(nodes['tl_title'],'resource',params['title_img'])

    # set footer image
    set_text(nodes['pl_foot_img'],'resource',params['foot_img'])
    set_text(nodes['tl_foot'],'resource',params['foot_img'])

    tree.write(output)

    # import code; code.interact(local=locals())

"""
pl = tree[1]['main bin']
for pi in pl.findall("entry[@sample]"): 
    print( pi.tag, pi.get('producer') )
    tree[0].remove(pi)

"""

def test():

    params = {
        'title_img': '/home/carl/Videos/veyepar/dot_net_fringe/dot_net_fringe_2015/titles/On_the_fringe_of_Nodejs_and_NET_with_Edgejs.png',
        'foot_img': 'bling/fosdem_2014_foot.png',
        'clips':[
                {'id':'123',
                'filename':'/home/carl/Videos/veyepar/dot_net_fringe/dot_net_fringe_2015/dv/main_stage/2015-04-14/09_02_51.dv',
                }
            ],
        'cuts':[{'id':'456',
                'filename':'/home/carl/Videos/veyepar/dot_net_fringe/dot_net_fringe_2015/dv/main_stage/2015-04-14/09_02_51.dv',
                'in':1,
                'out':None,
                },], 
        'audio_level': None,
        'channel_copy': None,
        }

    mk_mlt("template.mlt", "test.mlt",  params)
    return 

    params = {
        'title_img': '/home/carl/Videos/veyepar/test_client/test_show/titles/Lets_make_a_Test.png',
        'foot_img': 'bling/ndv-169.png',
        'clips':[
                {'id':'123',
                'filename':'/home/carl/Videos/veyepar/dot_net_fringe/dot_net_fringe_2015/dv/main_stage/2015-04-14/09_02_51.dv',
                }
            ],
        'cuts':[{'id':'456',
                'filename':'/home/carl/Videos/veyepar/dot_net_fringe/dot_net_fringe_2015/dv/main_stage/2015-04-14/09_02_51.dv',
                'in':1,
                'out':None,
                },], 
        'audio_level': None,
        'channel_copy': None,
        }

    for i in range(5):
        params['clips'].append({'id':str(i),
            'filename':'/home/carl/Videos/veyepar/test_client/test_show/dv/test_loc/2010-05-21/00_00_03.dv',
                'in':1,
                'out':2,
                })

    mk_mlt("template.mlt", "test.mlt",  params)


if __name__ == '__main__':
    test()
