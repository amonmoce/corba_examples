# Python stubs generated by omniidl from ../echo.idl
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
# Start of module "Example"
#
__name__ = "Example"
_0_Example = omniORB.openModule("Example", r"../echo.idl")
_0_Example__POA = omniORB.openModule("Example__POA", r"../echo.idl")


# interface Echo
_0_Example._d_Echo = (omniORB.tcInternal.tv_objref, "IDL:Example/Echo:1.0", "Echo")
omniORB.typeMapping["IDL:Example/Echo:1.0"] = _0_Example._d_Echo
_0_Example.Echo = omniORB.newEmptyClass()
class Echo :
    _NP_RepositoryId = _0_Example._d_Echo[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_Example.Echo = Echo
_0_Example._tc_Echo = omniORB.tcInternal.createTypeCode(_0_Example._d_Echo)
omniORB.registerType(Echo._NP_RepositoryId, _0_Example._d_Echo, _0_Example._tc_Echo)

# Echo operations and attributes
Echo._d_echoString = (((omniORB.tcInternal.tv_string,0), ), ((omniORB.tcInternal.tv_string,0), ), None)

# Echo object reference
class _objref_Echo (CORBA.Object):
    _NP_RepositoryId = Echo._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def echoString(self, *args):
        return self._obj.invoke("echoString", _0_Example.Echo._d_echoString, args)

omniORB.registerObjref(Echo._NP_RepositoryId, _objref_Echo)
_0_Example._objref_Echo = _objref_Echo
del Echo, _objref_Echo

# Echo skeleton
__name__ = "Example__POA"
class Echo (PortableServer.Servant):
    _NP_RepositoryId = _0_Example.Echo._NP_RepositoryId


    _omni_op_d = {"echoString": _0_Example.Echo._d_echoString}

Echo._omni_skeleton = Echo
_0_Example__POA.Echo = Echo
omniORB.registerSkeleton(Echo._NP_RepositoryId, Echo)
del Echo
__name__ = "Example"

#
# End of module "Example"
#
__name__ = "echo_idl"

_exported_modules = ( "Example", )

# The end.
