# Python stubs generated by omniidl from /usr/local/share/idl/omniORB/COS/CosGraphs.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


# #include "corbaidl.idl"
import corbaidl_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "boxes.idl"
import boxes_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "ir.idl"
import ir_idl
_0_CORBA = omniORB.openModule("CORBA")
_0_CORBA__POA = omniORB.openModule("CORBA__POA")

# #include "CosObjectIdentity.idl"
import CosObjectIdentity_idl
_0_CosObjectIdentity = omniORB.openModule("CosObjectIdentity")
_0_CosObjectIdentity__POA = omniORB.openModule("CosObjectIdentity__POA")

# #include "CosRelationships.idl"
import CosRelationships_idl
_0_CosRelationships = omniORB.openModule("CosRelationships")
_0_CosRelationships__POA = omniORB.openModule("CosRelationships__POA")

#
# Start of module "CosGraphs"
#
__name__ = "CosGraphs"
_0_CosGraphs = omniORB.openModule("CosGraphs", r"/usr/local/share/idl/omniORB/COS/CosGraphs.idl")
_0_CosGraphs__POA = omniORB.openModule("CosGraphs__POA", r"/usr/local/share/idl/omniORB/COS/CosGraphs.idl")


# forward interface TraversalFactory;
_0_CosGraphs._d_TraversalFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/TraversalFactory:1.0", "TraversalFactory")
omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalFactory:1.0"] = _0_CosGraphs._d_TraversalFactory

# forward interface Traversal;
_0_CosGraphs._d_Traversal = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/Traversal:1.0", "Traversal")
omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal:1.0"] = _0_CosGraphs._d_Traversal

# forward interface TraversalCriteria;
_0_CosGraphs._d_TraversalCriteria = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/TraversalCriteria:1.0", "TraversalCriteria")
omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria:1.0"] = _0_CosGraphs._d_TraversalCriteria

# forward interface Node;
_0_CosGraphs._d_Node = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/Node:1.0", "Node")
omniORB.typeMapping["IDL:omg.org/CosGraphs/Node:1.0"] = _0_CosGraphs._d_Node

# forward interface NodeFactory;
_0_CosGraphs._d_NodeFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/NodeFactory:1.0", "NodeFactory")
omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeFactory:1.0"] = _0_CosGraphs._d_NodeFactory

# forward interface Role;
_0_CosGraphs._d_Role = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/Role:1.0", "Role")
omniORB.typeMapping["IDL:omg.org/CosGraphs/Role:1.0"] = _0_CosGraphs._d_Role

# forward interface EdgeIterator;
_0_CosGraphs._d_EdgeIterator = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/EdgeIterator:1.0", "EdgeIterator")
omniORB.typeMapping["IDL:omg.org/CosGraphs/EdgeIterator:1.0"] = _0_CosGraphs._d_EdgeIterator

# struct NodeHandle
_0_CosGraphs.NodeHandle = omniORB.newEmptyClass()
class NodeHandle (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/NodeHandle:1.0"

    def __init__(self, the_node, constant_random_id):
        self.the_node = the_node
        self.constant_random_id = constant_random_id

_0_CosGraphs.NodeHandle = NodeHandle
_0_CosGraphs._d_NodeHandle  = (omniORB.tcInternal.tv_struct, NodeHandle, NodeHandle._NP_RepositoryId, "NodeHandle", "the_node", omniORB.typeMapping["IDL:omg.org/CosGraphs/Node:1.0"], "constant_random_id", omniORB.typeMapping["IDL:omg.org/CosObjectIdentity/ObjectIdentifier:1.0"])
_0_CosGraphs._tc_NodeHandle = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_NodeHandle)
omniORB.registerType(NodeHandle._NP_RepositoryId, _0_CosGraphs._d_NodeHandle, _0_CosGraphs._tc_NodeHandle)
del NodeHandle

# typedef ... NodeHandles
class NodeHandles:
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/NodeHandles:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosGraphs.NodeHandles = NodeHandles
_0_CosGraphs._d_NodeHandles  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeHandle:1.0"], 0)
_0_CosGraphs._ad_NodeHandles = (omniORB.tcInternal.tv_alias, NodeHandles._NP_RepositoryId, "NodeHandles", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeHandle:1.0"], 0))
_0_CosGraphs._tc_NodeHandles = omniORB.tcInternal.createTypeCode(_0_CosGraphs._ad_NodeHandles)
omniORB.registerType(NodeHandles._NP_RepositoryId, _0_CosGraphs._ad_NodeHandles, _0_CosGraphs._tc_NodeHandles)
del NodeHandles

# struct NamedRole
_0_CosGraphs.NamedRole = omniORB.newEmptyClass()
class NamedRole (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/NamedRole:1.0"

    def __init__(self, the_role, the_name):
        self.the_role = the_role
        self.the_name = the_name

_0_CosGraphs.NamedRole = NamedRole
_0_CosGraphs._d_NamedRole  = (omniORB.tcInternal.tv_struct, NamedRole, NamedRole._NP_RepositoryId, "NamedRole", "the_role", omniORB.typeMapping["IDL:omg.org/CosGraphs/Role:1.0"], "the_name", omniORB.typeMapping["IDL:omg.org/CosRelationships/RoleName:1.0"])
_0_CosGraphs._tc_NamedRole = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_NamedRole)
omniORB.registerType(NamedRole._NP_RepositoryId, _0_CosGraphs._d_NamedRole, _0_CosGraphs._tc_NamedRole)
del NamedRole

# typedef ... NamedRoles
class NamedRoles:
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/NamedRoles:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosGraphs.NamedRoles = NamedRoles
_0_CosGraphs._d_NamedRoles  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/NamedRole:1.0"], 0)
_0_CosGraphs._ad_NamedRoles = (omniORB.tcInternal.tv_alias, NamedRoles._NP_RepositoryId, "NamedRoles", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/NamedRole:1.0"], 0))
_0_CosGraphs._tc_NamedRoles = omniORB.tcInternal.createTypeCode(_0_CosGraphs._ad_NamedRoles)
omniORB.registerType(NamedRoles._NP_RepositoryId, _0_CosGraphs._ad_NamedRoles, _0_CosGraphs._tc_NamedRoles)
del NamedRoles

# struct EndPoint
_0_CosGraphs.EndPoint = omniORB.newEmptyClass()
class EndPoint (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/EndPoint:1.0"

    def __init__(self, the_node, the_role):
        self.the_node = the_node
        self.the_role = the_role

_0_CosGraphs.EndPoint = EndPoint
_0_CosGraphs._d_EndPoint  = (omniORB.tcInternal.tv_struct, EndPoint, EndPoint._NP_RepositoryId, "EndPoint", "the_node", omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeHandle:1.0"], "the_role", omniORB.typeMapping["IDL:omg.org/CosGraphs/NamedRole:1.0"])
_0_CosGraphs._tc_EndPoint = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_EndPoint)
omniORB.registerType(EndPoint._NP_RepositoryId, _0_CosGraphs._d_EndPoint, _0_CosGraphs._tc_EndPoint)
del EndPoint

# typedef ... EndPoints
class EndPoints:
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/EndPoints:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosGraphs.EndPoints = EndPoints
_0_CosGraphs._d_EndPoints  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/EndPoint:1.0"], 0)
_0_CosGraphs._ad_EndPoints = (omniORB.tcInternal.tv_alias, EndPoints._NP_RepositoryId, "EndPoints", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/EndPoint:1.0"], 0))
_0_CosGraphs._tc_EndPoints = omniORB.tcInternal.createTypeCode(_0_CosGraphs._ad_EndPoints)
omniORB.registerType(EndPoints._NP_RepositoryId, _0_CosGraphs._ad_EndPoints, _0_CosGraphs._tc_EndPoints)
del EndPoints

# struct Edge
_0_CosGraphs.Edge = omniORB.newEmptyClass()
class Edge (omniORB.StructBase):
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/Edge:1.0"

    def __init__(self, _from, the_relationship, relatives):
        self._from = _from
        self.the_relationship = the_relationship
        self.relatives = relatives

_0_CosGraphs.Edge = Edge
_0_CosGraphs._d_Edge  = (omniORB.tcInternal.tv_struct, Edge, Edge._NP_RepositoryId, "Edge", "_from", omniORB.typeMapping["IDL:omg.org/CosGraphs/EndPoint:1.0"], "the_relationship", omniORB.typeMapping["IDL:omg.org/CosRelationships/RelationshipHandle:1.0"], "relatives", omniORB.typeMapping["IDL:omg.org/CosGraphs/EndPoints:1.0"])
_0_CosGraphs._tc_Edge = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_Edge)
omniORB.registerType(Edge._NP_RepositoryId, _0_CosGraphs._d_Edge, _0_CosGraphs._tc_Edge)
del Edge

# typedef ... Edges
class Edges:
    _NP_RepositoryId = "IDL:omg.org/CosGraphs/Edges:1.0"
    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")
_0_CosGraphs.Edges = Edges
_0_CosGraphs._d_Edges  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Edge:1.0"], 0)
_0_CosGraphs._ad_Edges = (omniORB.tcInternal.tv_alias, Edges._NP_RepositoryId, "Edges", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Edge:1.0"], 0))
_0_CosGraphs._tc_Edges = omniORB.tcInternal.createTypeCode(_0_CosGraphs._ad_Edges)
omniORB.registerType(Edges._NP_RepositoryId, _0_CosGraphs._ad_Edges, _0_CosGraphs._tc_Edges)
del Edges

# enum PropagationValue
_0_CosGraphs.deep = omniORB.EnumItem("deep", 0)
_0_CosGraphs.shallow = omniORB.EnumItem("shallow", 1)
_0_CosGraphs.none = omniORB.EnumItem("none", 2)
_0_CosGraphs.inhibit = omniORB.EnumItem("inhibit", 3)
_0_CosGraphs.PropagationValue = omniORB.Enum("IDL:omg.org/CosGraphs/PropagationValue:1.0", (_0_CosGraphs.deep, _0_CosGraphs.shallow, _0_CosGraphs.none, _0_CosGraphs.inhibit,))

_0_CosGraphs._d_PropagationValue  = (omniORB.tcInternal.tv_enum, _0_CosGraphs.PropagationValue._NP_RepositoryId, "PropagationValue", _0_CosGraphs.PropagationValue._items)
_0_CosGraphs._tc_PropagationValue = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_PropagationValue)
omniORB.registerType(_0_CosGraphs.PropagationValue._NP_RepositoryId, _0_CosGraphs._d_PropagationValue, _0_CosGraphs._tc_PropagationValue)

# enum Mode
_0_CosGraphs.depthFirst = omniORB.EnumItem("depthFirst", 0)
_0_CosGraphs.breadthFirst = omniORB.EnumItem("breadthFirst", 1)
_0_CosGraphs.bestFirst = omniORB.EnumItem("bestFirst", 2)
_0_CosGraphs.Mode = omniORB.Enum("IDL:omg.org/CosGraphs/Mode:1.0", (_0_CosGraphs.depthFirst, _0_CosGraphs.breadthFirst, _0_CosGraphs.bestFirst,))

_0_CosGraphs._d_Mode  = (omniORB.tcInternal.tv_enum, _0_CosGraphs.Mode._NP_RepositoryId, "Mode", _0_CosGraphs.Mode._items)
_0_CosGraphs._tc_Mode = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_Mode)
omniORB.registerType(_0_CosGraphs.Mode._NP_RepositoryId, _0_CosGraphs._d_Mode, _0_CosGraphs._tc_Mode)

# interface TraversalFactory
_0_CosGraphs._d_TraversalFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/TraversalFactory:1.0", "TraversalFactory")
omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalFactory:1.0"] = _0_CosGraphs._d_TraversalFactory
_0_CosGraphs.TraversalFactory = omniORB.newEmptyClass()
class TraversalFactory :
    _NP_RepositoryId = _0_CosGraphs._d_TraversalFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosGraphs.TraversalFactory = TraversalFactory
_0_CosGraphs._tc_TraversalFactory = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_TraversalFactory)
omniORB.registerType(TraversalFactory._NP_RepositoryId, _0_CosGraphs._d_TraversalFactory, _0_CosGraphs._tc_TraversalFactory)

# TraversalFactory operations and attributes
TraversalFactory._d_create_traversal_on = ((omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeHandle:1.0"], omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria:1.0"], omniORB.typeMapping["IDL:omg.org/CosGraphs/Mode:1.0"]), (omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal:1.0"], ), None)

# TraversalFactory object reference
class _objref_TraversalFactory (CORBA.Object):
    _NP_RepositoryId = TraversalFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create_traversal_on(self, *args):
        return self._obj.invoke("create_traversal_on", _0_CosGraphs.TraversalFactory._d_create_traversal_on, args)

omniORB.registerObjref(TraversalFactory._NP_RepositoryId, _objref_TraversalFactory)
_0_CosGraphs._objref_TraversalFactory = _objref_TraversalFactory
del TraversalFactory, _objref_TraversalFactory

# TraversalFactory skeleton
__name__ = "CosGraphs__POA"
class TraversalFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosGraphs.TraversalFactory._NP_RepositoryId


    _omni_op_d = {"create_traversal_on": _0_CosGraphs.TraversalFactory._d_create_traversal_on}

TraversalFactory._omni_skeleton = TraversalFactory
_0_CosGraphs__POA.TraversalFactory = TraversalFactory
omniORB.registerSkeleton(TraversalFactory._NP_RepositoryId, TraversalFactory)
del TraversalFactory
__name__ = "CosGraphs"

# interface Traversal
_0_CosGraphs._d_Traversal = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/Traversal:1.0", "Traversal")
omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal:1.0"] = _0_CosGraphs._d_Traversal
_0_CosGraphs.Traversal = omniORB.newEmptyClass()
class Traversal :
    _NP_RepositoryId = _0_CosGraphs._d_Traversal[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # typedef ... TraversalScopedId
    class TraversalScopedId:
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Traversal/TraversalScopedId:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_TraversalScopedId  = omniORB.tcInternal.tv_ulong
    _ad_TraversalScopedId = (omniORB.tcInternal.tv_alias, TraversalScopedId._NP_RepositoryId, "TraversalScopedId", omniORB.tcInternal.tv_ulong)
    _tc_TraversalScopedId = omniORB.tcInternal.createTypeCode(_ad_TraversalScopedId)
    omniORB.registerType(TraversalScopedId._NP_RepositoryId, _ad_TraversalScopedId, _tc_TraversalScopedId)
    
    # struct ScopedEndPoint
    _0_CosGraphs.Traversal.ScopedEndPoint = omniORB.newEmptyClass()
    class ScopedEndPoint (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Traversal/ScopedEndPoint:1.0"

        _NP_ClassName = "CosGraphs.Traversal.ScopedEndPoint"

        def __init__(self, point, id):
            self.point = point
            self.id = id
    
    _d_ScopedEndPoint  = _0_CosGraphs.Traversal._d_ScopedEndPoint = (omniORB.tcInternal.tv_struct, ScopedEndPoint, ScopedEndPoint._NP_RepositoryId, "ScopedEndPoint", "point", omniORB.typeMapping["IDL:omg.org/CosGraphs/EndPoint:1.0"], "id", omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/TraversalScopedId:1.0"])
    _tc_ScopedEndPoint = omniORB.tcInternal.createTypeCode(_d_ScopedEndPoint)
    omniORB.registerType(ScopedEndPoint._NP_RepositoryId, _d_ScopedEndPoint, _tc_ScopedEndPoint)
    
    # typedef ... ScopedEndPoints
    class ScopedEndPoints:
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Traversal/ScopedEndPoints:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_ScopedEndPoints  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEndPoint:1.0"], 0)
    _ad_ScopedEndPoints = (omniORB.tcInternal.tv_alias, ScopedEndPoints._NP_RepositoryId, "ScopedEndPoints", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEndPoint:1.0"], 0))
    _tc_ScopedEndPoints = omniORB.tcInternal.createTypeCode(_ad_ScopedEndPoints)
    omniORB.registerType(ScopedEndPoints._NP_RepositoryId, _ad_ScopedEndPoints, _tc_ScopedEndPoints)
    
    # struct ScopedRelationship
    _0_CosGraphs.Traversal.ScopedRelationship = omniORB.newEmptyClass()
    class ScopedRelationship (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Traversal/ScopedRelationship:1.0"

        _NP_ClassName = "CosGraphs.Traversal.ScopedRelationship"

        def __init__(self, scoped_relationship, id):
            self.scoped_relationship = scoped_relationship
            self.id = id
    
    _d_ScopedRelationship  = _0_CosGraphs.Traversal._d_ScopedRelationship = (omniORB.tcInternal.tv_struct, ScopedRelationship, ScopedRelationship._NP_RepositoryId, "ScopedRelationship", "scoped_relationship", omniORB.typeMapping["IDL:omg.org/CosRelationships/RelationshipHandle:1.0"], "id", omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/TraversalScopedId:1.0"])
    _tc_ScopedRelationship = omniORB.tcInternal.createTypeCode(_d_ScopedRelationship)
    omniORB.registerType(ScopedRelationship._NP_RepositoryId, _d_ScopedRelationship, _tc_ScopedRelationship)
    
    # struct ScopedEdge
    _0_CosGraphs.Traversal.ScopedEdge = omniORB.newEmptyClass()
    class ScopedEdge (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Traversal/ScopedEdge:1.0"

        _NP_ClassName = "CosGraphs.Traversal.ScopedEdge"

        def __init__(self, _from, the_relationship, relatives):
            self._from = _from
            self.the_relationship = the_relationship
            self.relatives = relatives
    
    _d_ScopedEdge  = _0_CosGraphs.Traversal._d_ScopedEdge = (omniORB.tcInternal.tv_struct, ScopedEdge, ScopedEdge._NP_RepositoryId, "ScopedEdge", "_from", omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEndPoint:1.0"], "the_relationship", omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedRelationship:1.0"], "relatives", omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEndPoints:1.0"])
    _tc_ScopedEdge = omniORB.tcInternal.createTypeCode(_d_ScopedEdge)
    omniORB.registerType(ScopedEdge._NP_RepositoryId, _d_ScopedEdge, _tc_ScopedEdge)
    
    # typedef ... ScopedEdges
    class ScopedEdges:
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Traversal/ScopedEdges:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_ScopedEdges  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEdge:1.0"], 0)
    _ad_ScopedEdges = (omniORB.tcInternal.tv_alias, ScopedEdges._NP_RepositoryId, "ScopedEdges", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEdge:1.0"], 0))
    _tc_ScopedEdges = omniORB.tcInternal.createTypeCode(_ad_ScopedEdges)
    omniORB.registerType(ScopedEdges._NP_RepositoryId, _ad_ScopedEdges, _tc_ScopedEdges)


_0_CosGraphs.Traversal = Traversal
_0_CosGraphs._tc_Traversal = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_Traversal)
omniORB.registerType(Traversal._NP_RepositoryId, _0_CosGraphs._d_Traversal, _0_CosGraphs._tc_Traversal)

# Traversal operations and attributes
Traversal._d_next_one = ((), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEdge:1.0"]), None)
Traversal._d_next_n = ((omniORB.tcInternal.tv_short, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:omg.org/CosGraphs/Traversal/ScopedEdges:1.0"]), None)
Traversal._d_destroy = ((), (), None)

# Traversal object reference
class _objref_Traversal (CORBA.Object):
    _NP_RepositoryId = Traversal._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_one(self, *args):
        return self._obj.invoke("next_one", _0_CosGraphs.Traversal._d_next_one, args)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_CosGraphs.Traversal._d_next_n, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_CosGraphs.Traversal._d_destroy, args)

omniORB.registerObjref(Traversal._NP_RepositoryId, _objref_Traversal)
_0_CosGraphs._objref_Traversal = _objref_Traversal
del Traversal, _objref_Traversal

# Traversal skeleton
__name__ = "CosGraphs__POA"
class Traversal (PortableServer.Servant):
    _NP_RepositoryId = _0_CosGraphs.Traversal._NP_RepositoryId


    _omni_op_d = {"next_one": _0_CosGraphs.Traversal._d_next_one, "next_n": _0_CosGraphs.Traversal._d_next_n, "destroy": _0_CosGraphs.Traversal._d_destroy}

Traversal._omni_skeleton = Traversal
_0_CosGraphs__POA.Traversal = Traversal
omniORB.registerSkeleton(Traversal._NP_RepositoryId, Traversal)
del Traversal
__name__ = "CosGraphs"

# interface TraversalCriteria
_0_CosGraphs._d_TraversalCriteria = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/TraversalCriteria:1.0", "TraversalCriteria")
omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria:1.0"] = _0_CosGraphs._d_TraversalCriteria
_0_CosGraphs.TraversalCriteria = omniORB.newEmptyClass()
class TraversalCriteria :
    _NP_RepositoryId = _0_CosGraphs._d_TraversalCriteria[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # struct WeightedEdge
    _0_CosGraphs.TraversalCriteria.WeightedEdge = omniORB.newEmptyClass()
    class WeightedEdge (omniORB.StructBase):
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/TraversalCriteria/WeightedEdge:1.0"

        _NP_ClassName = "CosGraphs.TraversalCriteria.WeightedEdge"

        def __init__(self, the_edge, weight, next_nodes):
            self.the_edge = the_edge
            self.weight = weight
            self.next_nodes = next_nodes
    
    _d_WeightedEdge  = _0_CosGraphs.TraversalCriteria._d_WeightedEdge = (omniORB.tcInternal.tv_struct, WeightedEdge, WeightedEdge._NP_RepositoryId, "WeightedEdge", "the_edge", omniORB.typeMapping["IDL:omg.org/CosGraphs/Edge:1.0"], "weight", omniORB.tcInternal.tv_ulong, "next_nodes", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeHandle:1.0"], 0))
    _tc_WeightedEdge = omniORB.tcInternal.createTypeCode(_d_WeightedEdge)
    omniORB.registerType(WeightedEdge._NP_RepositoryId, _d_WeightedEdge, _tc_WeightedEdge)
    
    # typedef ... WeightedEdges
    class WeightedEdges:
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/TraversalCriteria/WeightedEdges:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_WeightedEdges  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria/WeightedEdge:1.0"], 0)
    _ad_WeightedEdges = (omniORB.tcInternal.tv_alias, WeightedEdges._NP_RepositoryId, "WeightedEdges", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria/WeightedEdge:1.0"], 0))
    _tc_WeightedEdges = omniORB.tcInternal.createTypeCode(_ad_WeightedEdges)
    omniORB.registerType(WeightedEdges._NP_RepositoryId, _ad_WeightedEdges, _tc_WeightedEdges)


_0_CosGraphs.TraversalCriteria = TraversalCriteria
_0_CosGraphs._tc_TraversalCriteria = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_TraversalCriteria)
omniORB.registerType(TraversalCriteria._NP_RepositoryId, _0_CosGraphs._d_TraversalCriteria, _0_CosGraphs._tc_TraversalCriteria)

# TraversalCriteria operations and attributes
TraversalCriteria._d_visit_node = ((omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeHandle:1.0"], omniORB.typeMapping["IDL:omg.org/CosGraphs/Mode:1.0"]), (), None)
TraversalCriteria._d_next_one = ((), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria/WeightedEdge:1.0"]), None)
TraversalCriteria._d_next_n = ((omniORB.tcInternal.tv_short, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:omg.org/CosGraphs/TraversalCriteria/WeightedEdges:1.0"]), None)
TraversalCriteria._d_destroy = ((), (), None)

# TraversalCriteria object reference
class _objref_TraversalCriteria (CORBA.Object):
    _NP_RepositoryId = TraversalCriteria._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def visit_node(self, *args):
        return self._obj.invoke("visit_node", _0_CosGraphs.TraversalCriteria._d_visit_node, args)

    def next_one(self, *args):
        return self._obj.invoke("next_one", _0_CosGraphs.TraversalCriteria._d_next_one, args)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_CosGraphs.TraversalCriteria._d_next_n, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_CosGraphs.TraversalCriteria._d_destroy, args)

omniORB.registerObjref(TraversalCriteria._NP_RepositoryId, _objref_TraversalCriteria)
_0_CosGraphs._objref_TraversalCriteria = _objref_TraversalCriteria
del TraversalCriteria, _objref_TraversalCriteria

# TraversalCriteria skeleton
__name__ = "CosGraphs__POA"
class TraversalCriteria (PortableServer.Servant):
    _NP_RepositoryId = _0_CosGraphs.TraversalCriteria._NP_RepositoryId


    _omni_op_d = {"visit_node": _0_CosGraphs.TraversalCriteria._d_visit_node, "next_one": _0_CosGraphs.TraversalCriteria._d_next_one, "next_n": _0_CosGraphs.TraversalCriteria._d_next_n, "destroy": _0_CosGraphs.TraversalCriteria._d_destroy}

TraversalCriteria._omni_skeleton = TraversalCriteria
_0_CosGraphs__POA.TraversalCriteria = TraversalCriteria
omniORB.registerSkeleton(TraversalCriteria._NP_RepositoryId, TraversalCriteria)
del TraversalCriteria
__name__ = "CosGraphs"

# interface Node
_0_CosGraphs._d_Node = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/Node:1.0", "Node")
omniORB.typeMapping["IDL:omg.org/CosGraphs/Node:1.0"] = _0_CosGraphs._d_Node
_0_CosGraphs.Node = omniORB.newEmptyClass()
class Node (_0_CosObjectIdentity.IdentifiableObject):
    _NP_RepositoryId = _0_CosGraphs._d_Node[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil

    
    # typedef ... Roles
    class Roles:
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Node/Roles:1.0"
        def __init__(self, *args, **kw):
            raise RuntimeError("Cannot construct objects of this type.")
    _d_Roles  = (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Role:1.0"], 0)
    _ad_Roles = (omniORB.tcInternal.tv_alias, Roles._NP_RepositoryId, "Roles", (omniORB.tcInternal.tv_sequence, omniORB.typeMapping["IDL:omg.org/CosGraphs/Role:1.0"], 0))
    _tc_Roles = omniORB.tcInternal.createTypeCode(_ad_Roles)
    omniORB.registerType(Roles._NP_RepositoryId, _ad_Roles, _tc_Roles)
    
    # exception NoSuchRole
    _0_CosGraphs.Node.NoSuchRole = omniORB.newEmptyClass()
    class NoSuchRole (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Node/NoSuchRole:1.0"

        _NP_ClassName = "CosGraphs.Node.NoSuchRole"

        def __init__(self):
            CORBA.UserException.__init__(self)
    
    _d_NoSuchRole  = (omniORB.tcInternal.tv_except, NoSuchRole, NoSuchRole._NP_RepositoryId, "NoSuchRole")
    _tc_NoSuchRole = omniORB.tcInternal.createTypeCode(_d_NoSuchRole)
    omniORB.registerType(NoSuchRole._NP_RepositoryId, _d_NoSuchRole, _tc_NoSuchRole)
    
    # exception DuplicateRoleType
    _0_CosGraphs.Node.DuplicateRoleType = omniORB.newEmptyClass()
    class DuplicateRoleType (CORBA.UserException):
        _NP_RepositoryId = "IDL:omg.org/CosGraphs/Node/DuplicateRoleType:1.0"

        _NP_ClassName = "CosGraphs.Node.DuplicateRoleType"

        def __init__(self):
            CORBA.UserException.__init__(self)
    
    _d_DuplicateRoleType  = (omniORB.tcInternal.tv_except, DuplicateRoleType, DuplicateRoleType._NP_RepositoryId, "DuplicateRoleType")
    _tc_DuplicateRoleType = omniORB.tcInternal.createTypeCode(_d_DuplicateRoleType)
    omniORB.registerType(DuplicateRoleType._NP_RepositoryId, _d_DuplicateRoleType, _tc_DuplicateRoleType)


_0_CosGraphs.Node = Node
_0_CosGraphs._tc_Node = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_Node)
omniORB.registerType(Node._NP_RepositoryId, _0_CosGraphs._d_Node, _0_CosGraphs._tc_Node)

# Node operations and attributes
Node._d__get_related_object = ((),(omniORB.typeMapping["IDL:omg.org/CosRelationships/RelatedObject:1.0"],),None)
Node._d__get_roles_of_node = ((),(omniORB.typeMapping["IDL:omg.org/CosGraphs/Node/Roles:1.0"],),None)
Node._d_roles_of_type = ((omniORB.typeMapping["IDL:omg.org/CORBA/InterfaceDef:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosGraphs/Node/Roles:1.0"], ), None)
Node._d_add_role = ((omniORB.typeMapping["IDL:omg.org/CosGraphs/Role:1.0"], ), (), {_0_CosGraphs.Node.DuplicateRoleType._NP_RepositoryId: _0_CosGraphs.Node._d_DuplicateRoleType})
Node._d_remove_role = ((omniORB.typeMapping["IDL:omg.org/CORBA/InterfaceDef:1.0"], ), (), {_0_CosGraphs.Node.NoSuchRole._NP_RepositoryId: _0_CosGraphs.Node._d_NoSuchRole})

# Node object reference
class _objref_Node (_0_CosObjectIdentity._objref_IdentifiableObject):
    _NP_RepositoryId = Node._NP_RepositoryId

    def __init__(self, obj):
        _0_CosObjectIdentity._objref_IdentifiableObject.__init__(self, obj)

    def _get_related_object(self, *args):
        return self._obj.invoke("_get_related_object", _0_CosGraphs.Node._d__get_related_object, args)

    related_object = property(_get_related_object)


    def _get_roles_of_node(self, *args):
        return self._obj.invoke("_get_roles_of_node", _0_CosGraphs.Node._d__get_roles_of_node, args)

    roles_of_node = property(_get_roles_of_node)


    def roles_of_type(self, *args):
        return self._obj.invoke("roles_of_type", _0_CosGraphs.Node._d_roles_of_type, args)

    def add_role(self, *args):
        return self._obj.invoke("add_role", _0_CosGraphs.Node._d_add_role, args)

    def remove_role(self, *args):
        return self._obj.invoke("remove_role", _0_CosGraphs.Node._d_remove_role, args)

omniORB.registerObjref(Node._NP_RepositoryId, _objref_Node)
_0_CosGraphs._objref_Node = _objref_Node
del Node, _objref_Node

# Node skeleton
__name__ = "CosGraphs__POA"
class Node (_0_CosObjectIdentity__POA.IdentifiableObject):
    _NP_RepositoryId = _0_CosGraphs.Node._NP_RepositoryId


    _omni_op_d = {"_get_related_object": _0_CosGraphs.Node._d__get_related_object, "_get_roles_of_node": _0_CosGraphs.Node._d__get_roles_of_node, "roles_of_type": _0_CosGraphs.Node._d_roles_of_type, "add_role": _0_CosGraphs.Node._d_add_role, "remove_role": _0_CosGraphs.Node._d_remove_role}
    _omni_op_d.update(_0_CosObjectIdentity__POA.IdentifiableObject._omni_op_d)

Node._omni_skeleton = Node
_0_CosGraphs__POA.Node = Node
omniORB.registerSkeleton(Node._NP_RepositoryId, Node)
del Node
__name__ = "CosGraphs"

# interface NodeFactory
_0_CosGraphs._d_NodeFactory = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/NodeFactory:1.0", "NodeFactory")
omniORB.typeMapping["IDL:omg.org/CosGraphs/NodeFactory:1.0"] = _0_CosGraphs._d_NodeFactory
_0_CosGraphs.NodeFactory = omniORB.newEmptyClass()
class NodeFactory :
    _NP_RepositoryId = _0_CosGraphs._d_NodeFactory[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosGraphs.NodeFactory = NodeFactory
_0_CosGraphs._tc_NodeFactory = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_NodeFactory)
omniORB.registerType(NodeFactory._NP_RepositoryId, _0_CosGraphs._d_NodeFactory, _0_CosGraphs._tc_NodeFactory)

# NodeFactory operations and attributes
NodeFactory._d_create_node = ((omniORB.typeMapping["IDL:omg.org/CORBA/Object:1.0"], ), (omniORB.typeMapping["IDL:omg.org/CosGraphs/Node:1.0"], ), None)

# NodeFactory object reference
class _objref_NodeFactory (CORBA.Object):
    _NP_RepositoryId = NodeFactory._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def create_node(self, *args):
        return self._obj.invoke("create_node", _0_CosGraphs.NodeFactory._d_create_node, args)

omniORB.registerObjref(NodeFactory._NP_RepositoryId, _objref_NodeFactory)
_0_CosGraphs._objref_NodeFactory = _objref_NodeFactory
del NodeFactory, _objref_NodeFactory

# NodeFactory skeleton
__name__ = "CosGraphs__POA"
class NodeFactory (PortableServer.Servant):
    _NP_RepositoryId = _0_CosGraphs.NodeFactory._NP_RepositoryId


    _omni_op_d = {"create_node": _0_CosGraphs.NodeFactory._d_create_node}

NodeFactory._omni_skeleton = NodeFactory
_0_CosGraphs__POA.NodeFactory = NodeFactory
omniORB.registerSkeleton(NodeFactory._NP_RepositoryId, NodeFactory)
del NodeFactory
__name__ = "CosGraphs"

# interface Role
_0_CosGraphs._d_Role = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/Role:1.0", "Role")
omniORB.typeMapping["IDL:omg.org/CosGraphs/Role:1.0"] = _0_CosGraphs._d_Role
_0_CosGraphs.Role = omniORB.newEmptyClass()
class Role (_0_CosRelationships.Role):
    _NP_RepositoryId = _0_CosGraphs._d_Role[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosGraphs.Role = Role
_0_CosGraphs._tc_Role = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_Role)
omniORB.registerType(Role._NP_RepositoryId, _0_CosGraphs._d_Role, _0_CosGraphs._tc_Role)

# Role operations and attributes
Role._d_get_edges = ((omniORB.tcInternal.tv_long, ), (omniORB.typeMapping["IDL:omg.org/CosGraphs/Edges:1.0"], omniORB.typeMapping["IDL:omg.org/CosGraphs/EdgeIterator:1.0"]), None)

# Role object reference
class _objref_Role (_0_CosRelationships._objref_Role):
    _NP_RepositoryId = Role._NP_RepositoryId

    def __init__(self, obj):
        _0_CosRelationships._objref_Role.__init__(self, obj)

    def get_edges(self, *args):
        return self._obj.invoke("get_edges", _0_CosGraphs.Role._d_get_edges, args)

omniORB.registerObjref(Role._NP_RepositoryId, _objref_Role)
_0_CosGraphs._objref_Role = _objref_Role
del Role, _objref_Role

# Role skeleton
__name__ = "CosGraphs__POA"
class Role (_0_CosRelationships__POA.Role):
    _NP_RepositoryId = _0_CosGraphs.Role._NP_RepositoryId


    _omni_op_d = {"get_edges": _0_CosGraphs.Role._d_get_edges}
    _omni_op_d.update(_0_CosRelationships__POA.Role._omni_op_d)

Role._omni_skeleton = Role
_0_CosGraphs__POA.Role = Role
omniORB.registerSkeleton(Role._NP_RepositoryId, Role)
del Role
__name__ = "CosGraphs"

# interface EdgeIterator
_0_CosGraphs._d_EdgeIterator = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosGraphs/EdgeIterator:1.0", "EdgeIterator")
omniORB.typeMapping["IDL:omg.org/CosGraphs/EdgeIterator:1.0"] = _0_CosGraphs._d_EdgeIterator
_0_CosGraphs.EdgeIterator = omniORB.newEmptyClass()
class EdgeIterator :
    _NP_RepositoryId = _0_CosGraphs._d_EdgeIterator[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosGraphs.EdgeIterator = EdgeIterator
_0_CosGraphs._tc_EdgeIterator = omniORB.tcInternal.createTypeCode(_0_CosGraphs._d_EdgeIterator)
omniORB.registerType(EdgeIterator._NP_RepositoryId, _0_CosGraphs._d_EdgeIterator, _0_CosGraphs._tc_EdgeIterator)

# EdgeIterator operations and attributes
EdgeIterator._d_next_one = ((), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:omg.org/CosGraphs/Edge:1.0"]), None)
EdgeIterator._d_next_n = ((omniORB.tcInternal.tv_ulong, ), (omniORB.tcInternal.tv_boolean, omniORB.typeMapping["IDL:omg.org/CosGraphs/Edges:1.0"]), None)
EdgeIterator._d_destroy = ((), (), None)

# EdgeIterator object reference
class _objref_EdgeIterator (CORBA.Object):
    _NP_RepositoryId = EdgeIterator._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def next_one(self, *args):
        return self._obj.invoke("next_one", _0_CosGraphs.EdgeIterator._d_next_one, args)

    def next_n(self, *args):
        return self._obj.invoke("next_n", _0_CosGraphs.EdgeIterator._d_next_n, args)

    def destroy(self, *args):
        return self._obj.invoke("destroy", _0_CosGraphs.EdgeIterator._d_destroy, args)

omniORB.registerObjref(EdgeIterator._NP_RepositoryId, _objref_EdgeIterator)
_0_CosGraphs._objref_EdgeIterator = _objref_EdgeIterator
del EdgeIterator, _objref_EdgeIterator

# EdgeIterator skeleton
__name__ = "CosGraphs__POA"
class EdgeIterator (PortableServer.Servant):
    _NP_RepositoryId = _0_CosGraphs.EdgeIterator._NP_RepositoryId


    _omni_op_d = {"next_one": _0_CosGraphs.EdgeIterator._d_next_one, "next_n": _0_CosGraphs.EdgeIterator._d_next_n, "destroy": _0_CosGraphs.EdgeIterator._d_destroy}

EdgeIterator._omni_skeleton = EdgeIterator
_0_CosGraphs__POA.EdgeIterator = EdgeIterator
omniORB.registerSkeleton(EdgeIterator._NP_RepositoryId, EdgeIterator)
del EdgeIterator
__name__ = "CosGraphs"

#
# End of module "CosGraphs"
#
__name__ = "CosGraphs_idl"

_exported_modules = ( "CosGraphs", )

# The end.
