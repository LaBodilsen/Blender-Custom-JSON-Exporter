Blender-JSON-Exporter

THIS IS A WIP AND NOT YET FULLY FUNCTIONAL

Only functionality is BSPtree, everything else is implemented.
=====================

Blender Custom JSON Exporter (.json)

### Wanted File Format when its done:
```
{
    "colours" : {
        "TAIL_COLOUR" : "COLOUR_WOODY_GREEN",
        "FUSELAGE_UPPER_COLOUR" : "COLOUR_DARK_WOODY_GREEN",
        "FUSELAGE_UPPER_SIDES_COLOUR" : "COLOUR_WOODY_GREEN",
//..
    },

    "vertices": [
        [     0,     0,     0 ],
        [ -5250,     0,     0 ],
        [ -5500,  -289,  -500 ],
        [ -5500,  -866,  -500 ],
//..
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
//..
       
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

    "shadowFaces" : [
        "canopyFrontLeftLowerFace",
        "canopyFrontLeftUpperFace",
        "canopyFrontFace",
        "canopyFrontRightUpperFace",
        "canopyFrontRightLowerFace",
        "canopyRearLeftLowerFace",
        "canopyRearLeftUpperFace",
//..
        "noseLowerRightFace"
    ],

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
                    "faces" : [
                        "lowerFuselageLeftFrontFace", "lowerFuselageLeftMiddleFace", "lowerFuselageLeftRearFace",
                        "lowerFuselageBottomFace",
                        "lowerFuselageRightFrontFace", "lowerFuselageRightMiddleFace", "lowerFuselageRightRearFace"
                    ]
                }
            }
        }
    }
}
```
