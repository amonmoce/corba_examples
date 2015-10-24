# Python stubs generated by omniidl from /usr/local/share/idl/omniORB/COS/CosPersistencePID.idl
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


#
# Start of module "CosPersistencePID"
#
__name__ = "CosPersistencePID"
_0_CosPersistencePID = omniORB.openModule("CosPersistencePID", r"/usr/local/share/idl/omniORB/COS/CosPersistencePID.idl")
_0_CosPersistencePID__POA = omniORB.openModule("CosPersistencePID__POA", r"/usr/local/share/idl/omniORB/COS/CosPersistencePID.idl")


# interface PID
_0_CosPersistencePID._d_PID = (omniORB.tcInternal.tv_objref, "IDL:omg.org/CosPersistencePID/PID:1.0", "PID")
omniORB.typeMapping["IDL:omg.org/CosPersistencePID/PID:1.0"] = _0_CosPersistencePID._d_PID
_0_CosPersistencePID.PID = omniORB.newEmptyClass()
class PID :
    _NP_RepositoryId = _0_CosPersistencePID._d_PID[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_CosPersistencePID.PID = PID
_0_CosPersistencePID._tc_PID = omniORB.tcInternal.createTypeCode(_0_CosPersistencePID._d_PID)
omniORB.registerType(PID._NP_RepositoryId, _0_CosPersistencePID._d_PID, _0_CosPersistencePID._tc_PID)

# PID operations and attributes
PID._d__get_datastore_type = ((),((omniORB.tcInternal.tv_string,0),),None)
PID._d__set_datastore_type = (((omniORB.tcInternal.tv_string,0),),(),None)
PID._d_get_PIDString = ((), ((omniORB.tcInternal.tv_string,0), ), None)

# PID object reference
class _objref_PID (CORBA.Object):
    _NP_RepositoryId = PID._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def _get_datastore_type(self, *args):
        return self._obj.invoke("_get_datastore_type", _0_CosPersistencePID.PID._d__get_datastore_type, args)

    def _set_datastore_type(self, *args):
        return self._obj.invoke("_set_datastore_type", _0_CosPersistencePID.PID._d__set_datastore_type, args)

    datastore_type = property(_get_datastore_type, _set_datastore_type)


    def get_PIDString(self, *args):
        return self._obj.invoke("get_PIDString", _0_CosPersistencePID.PID._d_get_PIDString, args)

omniORB.registerObjref(PID._NP_RepositoryId, _objref_PID)
_0_CosPersistencePID._objref_PID = _objref_PID
del PID, _objref_PID

# PID skeleton
__name__ = "CosPersistencePID__POA"
class PID (PortableServer.Servant):
    _NP_RepositoryId = _0_CosPersistencePID.PID._NP_RepositoryId


    _omni_op_d = {"_get_datastore_type": _0_CosPersistencePID.PID._d__get_datastore_type, "_set_datastore_type": _0_CosPersistencePID.PID._d__set_datastore_type, "get_PIDString": _0_CosPersistencePID.PID._d_get_PIDString}

PID._omni_skeleton = PID
_0_CosPersistencePID__POA.PID = PID
omniORB.registerSkeleton(PID._NP_RepositoryId, PID)
del PID
__name__ = "CosPersistencePID"

#
# End of module "CosPersistencePID"
#
__name__ = "CosPersistencePID_idl"

_exported_modules = ( "CosPersistencePID", )

# The end.
