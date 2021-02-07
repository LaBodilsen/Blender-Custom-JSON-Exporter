import bpy


# #####################################################
# Utils
# #####################################################

def write_file( fname, content ):
    out = open( fname, "w" )
    out.write( content )
    out.close()

def ensure_folder_exist( foldername ):
    if not os.access( foldername, os.R_OK|os.W_OK|os.X_OK ):
        os.makedirs( foldername )

def ensure_extension( filepath, extension ):
    if not filepath.lower().endswith( extension ):
        filepath += extension
    return filepath


# #####################################################
# Templates - mesh
# #####################################################

TEMPLATE_FILE = """\
{
    "colours" : {
        "TAIL_COLOUR" : "COLOUR_WOODY_GREEN",
        "FUSELAGE_UPPER_COLOUR" : "COLOUR_DARK_WOODY_GREEN",
        "FUSELAGE_UPPER_SIDES_COLOUR" : "COLOUR_WOODY_GREEN",
        "WING_UPPER_COLOUR" : "COLOUR_DARK_WOODY_GREEN",
        "NOSE_UPPER_COLOUR" : "COLOUR_LIGHT_GREY",
        "FUSELAGE_LOWER_COLOUR" : "COLOUR_LIGHT_GREY",
        "FUSELAGE_LOWER_SIDES_COLOUR" : "COLOUR_MEDIUM_GREY",
        "WING_LOWER_COLOUR" : "COLOUR_LIGHT_GREY",
        "NOSE_LOWER_COLOUR" : "COLOUR_LIGHT_GREY",
        "CANOPY_COLOUR" : "COLOUR_BLACK",
        "INTAKE_COLOUR" : "COLOUR_DARK_GREY",
        "FUSELAGE_REAR_COLOUR" : "COLOUR_DARK_GREY",
        "EXHAUST_COLOUR" : "COLOUR_DULL_RED"
    },

    "bspTreeRoot" : "%(objname)s",

    "vertices": [
        %(vertices)s
    ],

    "faces" : {
%(faces)s
    },
}
"""

TEMPLATE_FACE = """\
        "%(name)s" : {
            "colour" : "COLOUR",
            "vertices" : [%(index)s]
        },
"""

def flat_array( array ):
    
    return ", ".join( str( round( x, 6 ) ) for x in array )


def get_mesh_string( context, global_scale ):
    import bpy
    import bmesh

    vertices = []
    objfaces = []

    obj = context.active_object
    
    for verts in obj.data.vertices:
        vertices.append("[" +str(int(verts.co.x*global_scale))+", " 
                        +str(int(verts.co.y*global_scale))+", "
                        +str(int(verts.co.z*global_scale))+"]")

    
    for faces in obj.data.polygons:
        facename = "face"+str(faces.index)
        objfaces.append(TEMPLATE_FACE % {
            "name" : facename,
            "index" : flat_array( faces.vertices[:] ),
        })
        
    return TEMPLATE_FILE % {
        "objname" : obj.name,
        "vertices": ",\n        ".join(map(str, vertices )), #flat_array( vertices ),
        "faces": "".join( objfaces ),
    }


def export_mesh( obj, filepath, global_scale ):
    
    text = get_mesh_string( obj, global_scale )
    write_file( filepath, text )
    
    print("writing", filepath, "done")


# #####################################################
# Main
# #####################################################

def save( operator, context, filepath = "", use_selection=False, use_mesh_modifiers=True, global_matrix=None, global_scale=1000):
    filepath = ensure_extension( filepath, ".json")
    
    export_mesh( context, filepath, global_scale)
    
    return {"FINISHED"}