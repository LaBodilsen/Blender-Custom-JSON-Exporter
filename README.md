Blender-JSON-Exporter

THIS IS A WIP AND NOT YET FULLY FUNCTIONAL
=====================

Blender Custom JSON Exporter (.json)

OBS: please note that this fork, is now very far from the original in functionality, and is in now way the same addin anymore.  When it's done, i will move it to a new repo. 

### Wanted File Format when its done:

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

    "bspTreeRoot" : "eurofighterSection",

    "vertices": [
        [     0,     0,     0 ],
        [ -5250,     0,     0 ],
        [ -5500,  -289,  -500 ],
        [ -5500,  -866,  -500 ],
        [ -5250, -1155,     0 ],
        [ -5000,  -866,   500 ],
        [ -5000,  -289,   500 ],
        [ -5000,   289,   500 ],
        [ -5000,   866,   500 ],
        [ -5250,  1155,     0 ],
        [ -5500,   866,  -500 ],
        [ -5500,   289,  -500 ],
        [  7000,  -289,  -500 ],
        [  4750,  -447,  -737 ],
        [  4750,  -550, -1300 ],
        [  4750,     0, -1600 ],
        [  7000,   289,  -500 ],
        [  4750,   550, -1300 ],
        [  7000,   289,  -500 ],
        [  4750,   447,  -737 ],
        [  2250,  -289, -1000 ],
        [  2250,   289, -1000 ],
        [  9000,     0,     0 ],
        [  7000,  -577,     0 ],
        [  7000,   577,     0 ],
        [  2250, -1200,     0 ],
        [  2250,  -775,  -737 ],
        [  2250,   775,  -737 ],
        [  2250,  1200,     0 ],
        [ -5515,     0,  -529 ],
        [ -7000,     0, -3500 ],
        [ -6000,     0, -3500 ],
        [ -2514,     0,  -711 ],
        [  7000,     0,     0 ],
        [  5000, -2000,     0 ],
        [  4750, -2000,     0 ],
        [  5500,     0,     0 ],
        [  4750,  2000,     0 ],
        [  5000,  2000,     0 ],
        [  4750,     0,     0 ],
        [ -2250, -5500,     0 ],
        [ -4000, -5500,     0 ],
        [ -4000,  5500,     0 ],
        [ -2250,  5500,     0 ],
        [  4750,  -872,     0 ],
        [  4375,  -633,   500 ],
        [  4000, -1200,  1000 ],
        [  4375,   633,   500 ],
        [  4000,  1200,  1000 ],
        [  4750,   872,     0 ],
        [  7000,  -289,   500 ],
        [  7000,   289,   500 ]
    ],

    "faces" : {
        "leftExhaustFace" : {
            "colour" : "EXHAUST_COLOUR",
            "vertices" : [ 1, 2, 3, 4, 5, 6 ]
        },
        "rightExhaustFace" : {
            "colour" : "EXHAUST_COLOUR",
            "vertices" : [ 1, 7, 8, 9, 10, 11 ]
        },
        "canopyFrontLeftLowerFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 12, 13, 14 ]
        },
        "canopyFrontLeftUpperFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 12, 14, 15 ]
        },
        "canopyFrontFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 12, 15, 16 ]
        },
        "canopyFrontRightUpperFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 15, 17, 18 ]
        },
        "canopyFrontRightLowerFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 17, 19, 18 ]
        },
        "canopyRearLeftLowerFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 13, 20, 14 ]
        },
        "canopyRearLeftUpperFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 14, 20, 15 ]
        },
        "canopyRearFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 15, 20, 21 ]
        },
        "canopyRearRightUpperFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 15, 21, 17 ]
        },
        "canopyRearRightLowerFace" : {
            "colour" : "CANOPY_COLOUR",
            "vertices" : [ 17, 21, 19 ]
        },
        "noseUpperLeftFace" : {
            "colour" : "NOSE_UPPER_COLOUR",
            "vertices" : [ 12, 22, 23 ]
        },
        "noseUpperFace" : {
            "colour" : "NOSE_UPPER_COLOUR",
            "vertices" : [ 12, 16, 22 ]
        },
        "noseUpperRightFace" : {
            "colour" : "NOSE_UPPER_COLOUR",
            "vertices" : [ 18, 24, 22 ]
        },
        "cockpitLeftSideFace" : {
            "colour" : "FUSELAGE_UPPER_SIDES_COLOUR",
            "vertices" : [ 12, 23, 25, 26, 13 ]
        },
        "cockpitLeftUpperFace" : {
            "colour" : "FUSELAGE_UPPER_COLOUR",
            "vertices" : [ 13, 26, 20 ]
        },
        "cockpitRightUpperFace" : {
            "colour" : "FUSELAGE_UPPER_COLOUR",
            "vertices" : [ 19, 21, 27 ]
        },
        "cockpitRightSideFace" : {
            "colour" : "FUSELAGE_UPPER_SIDES_COLOUR",
            "vertices" : [ 18, 19, 27, 28, 24 ]
        },
        "tailLeftFace" : {
            "colour" : "TAIL_COLOUR",
            "vertices" : [ 29, 30, 31, 32 ]
        },
        "tailRightFace" : {
            "colour" : "TAIL_COLOUR",
            "vertices" : [ 29, 32, 31, 30 ]
        },
        "upperFuselageTopFace" : {
            "colour" : "FUSELAGE_UPPER_COLOUR",
            "vertices" : [ 3, 10, 21, 20 ]
        },
        "upperFuselageLeftLowerFace" : {
            "colour" : "FUSELAGE_UPPER_SIDES_COLOUR",
            "vertices" : [ 3, 26, 25, 4 ]
        },
        "upperFuselageLeftUpperFace" : {
            "colour" : "FUSELAGE_UPPER_COLOUR",
            "vertices" : [ 3, 20, 26 ]
        },
        "upperFuselageRightUpperFace" : {
            "colour" : "FUSELAGE_UPPER_COLOUR",
            "vertices" : [ 10, 27, 21]
        },
        "upperFuselageRightLowerFace" : {
            "colour" : "FUSELAGE_UPPER_SIDES_COLOUR",
            "vertices" : [ 9, 28, 27, 10 ]
        },
        "fuselageRearFace" : {
            "colour" : "FUSELAGE_REAR_COLOUR",
            "vertices" : [ 3, 4, 5, 8, 9, 10 ]
        },
        "leftCanardUpperFace" : {
            "colour" : "WING_UPPER_COLOUR",
            "vertices" : [ 33, 34, 35, 36 ]
        },
        "rightCanardUpperFace" : {
            "colour" : "WING_UPPER_COLOUR",
            "vertices" : [ 33, 36, 37, 38 ]
        },
        "wingsUpperFace" : {
            "colour" : "WING_UPPER_COLOUR",
            "vertices" : [ 39, 40, 41, 42, 43 ]
        },
        "leftCanardLowerFace" : {
            "colour" : "WING_LOWER_COLOUR",
            "vertices" : [ 33, 36, 35, 34 ]
        },
        "rightCanardLowerFace" : {
            "colour" : "WING_LOWER_COLOUR",
            "vertices" : [ 38, 37, 36, 33 ]
        },
        "wingsLowerFace" : {
            "colour" : "WING_LOWER_COLOUR",
            "vertices" : [39, 43, 42, 41, 40 ]
        },
        "intakeLeftFace" : {
            "colour" : "INTAKE_COLOUR",
            "vertices" : [ 44, 45, 46 ]
        },
        "intakeMiddleFace" : {
            "colour" : "INTAKE_COLOUR",
            "vertices" : [ 45, 47, 48, 46 ]
        },
        "intakeRightFace" : {
            "colour" : "INTAKE_COLOUR",
            "vertices" : [ 47, 49, 48 ]
        },
        "lowerFuselageLeftFrontFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 25, 44, 46 ]
        },
        "lowerFuselageLeftMiddleFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 4, 25, 46 ]
        },
        "lowerFuselageLeftRearFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 4, 46, 5 ]
        },
        "lowerFuselageBottomFace" : {
            "colour" : "FUSELAGE_LOWER_COLOUR",
            "vertices" : [ 5, 46, 48, 8 ]
        },
        "lowerFuselageRightFrontFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 28, 48, 49 ]
        },
        "lowerFuselageRightMiddleFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 9, 48, 28 ]
        },
        "lowerFuselageRightRearFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 8, 48, 9 ]
        },
        "cockpitLowerLeftFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 23, 50, 45, 44 ]
        },
        "cockpitLowerFace" : {
            "colour" : "FUSELAGE_LOWER_COLOUR",
            "vertices" : [ 45, 50, 51, 47 ]
        },
        "cockpitLowerRightFace" : {
            "colour" : "FUSELAGE_LOWER_SIDES_COLOUR",
            "vertices" : [ 24, 49, 47, 51 ]
        },
        "noseLowerLeftFace" : {
            "colour" : "NOSE_LOWER_COLOUR",
            "vertices" : [ 22, 50, 23 ]
        },
        "noseLowerFace" : {
            "colour" : "NOSE_LOWER_COLOUR",
            "vertices" : [ 22, 51, 50 ]
        },
        "noseLowerRightFace" : {
            "colour" : "NOSE_LOWER_COLOUR",
            "vertices" : [ 22, 24, 51 ]
        },
        
        "Canopy_Base" : {
            "vertices" : [ 16, 20, 19 ]
        },
        "Bulkhead" : {
            "vertices" : [ 28, 25, 21 ]
        },
        "XY_Plane" : {
            "vertices" : [ 33, 41, 42 ]
        }
    },

    "bspTree" : {
        "splittingPlane" : "fuselageRearFace",
        "above" : {
            "faces" : [ "leftExhaustFace", "rightExhaustFace" ]
        },
        "onFromAbove" : {
            "faces" : [ "fuselageRearFace" ]
        },
        "below" : {
            "splittingPlane" : "XY_Plane",
            "above" : {
                "splittingPlane" : "Bulkhead",
                "above" : {
                    "splittingPlane" : "Canopy_Base",
                    "above" : {
                        "faces" : [
                            "canopyFrontLeftLowerFace", "canopyFrontLeftUpperFace", "canopyFrontFace", "canopyFrontRightUpperFace", "canopyFrontRightLowerFace",
                            "canopyRearLeftLowerFace", "canopyRearLeftUpperFace", "canopyRearFace", "canopyRearRightUpperFace", "canopyRearRightLowerFace"
                        ]
                    },
                    "below" : {
                        "faces" : [
                            "noseUpperLeftFace", "noseUpperFace", "noseUpperRightFace",
                            "cockpitLeftSideFace", "cockpitLeftUpperFace", "cockpitRightUpperFace", "cockpitRightSideFace"
                        ]
                    }
                },
                "below" : {
                    "splittingPlane" : "upperFuselageTopFace",
                    "above" : {
                        "faces" : [ "tailLeftFace", "tailRightFace" ]
                    },
                    "onFromAbove" : {
                        "faces" : [ "upperFuselageTopFace" ]
                    },
                    "below" : {
                        "faces" : [ "upperFuselageLeftLowerFace", "upperFuselageLeftUpperFace", "upperFuselageRightUpperFace", "upperFuselageRightLowerFace" ]
                    }
                }
            },
            "onFromAbove" : {
                "faces" : [ "leftCanardUpperFace", "rightCanardUpperFace", "wingsUpperFace" ]
            },
            "onFromBelow" : {
                "faces" : [ "leftCanardLowerFace", "rightCanardLowerFace", "wingsLowerFace" ]
            },
            "below" : {
                "splittingPlane" : "intakeMiddleFace",
                "above" : {
                    "faces" : [ "cockpitLowerLeftFace", "cockpitLowerFace", "cockpitLowerRightFace", "noseLowerLeftFace", "noseLowerFace", "noseLowerRightFace" ]
                },
                "onFromAbove" : {
                    "faces" : [ "intakeLeftFace", "intakeMiddleFace", "intakeRightFace" ]
                },
                "below" : {
                    "faces" : [ "lowerFuselageLeftFrontFace", "lowerFuselageLeftMiddleFace", "lowerFuselageLeftRearFace",
                                "lowerFuselageBottomFace",
                                "lowerFuselageRightFrontFace", "lowerFuselageRightMiddleFace", "lowerFuselageRightRearFace"
                    ]
                }
            }
        }
    }

}
