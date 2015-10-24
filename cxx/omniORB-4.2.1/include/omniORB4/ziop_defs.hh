// This file is generated by omniidl (C++ backend)- omniORB_4_2. Do not edit.
#ifndef __ziop_defs_hh__
#define __ziop_defs_hh__

_CORBA_MODULE_VAR _dyn_attr const ::CORBA::TypeCode_ptr _tc_PolicyType;

typedef ::CORBA::ULong PolicyType;
typedef ::CORBA::ULong_out PolicyType_out;

struct CompressedData {
  typedef _CORBA_ConstrType_Variable_Var<CompressedData> _var_type;

  
  Compression::CompressorId compressorid;

  ::CORBA::ULong original_length;

  Compression::Buffer data;



  void operator>>= (cdrStream &) const;
  void operator<<= (cdrStream &);
};

typedef CompressedData::_var_type CompressedData_var;

typedef _CORBA_ConstrType_Variable_OUT_arg< CompressedData,CompressedData_var > CompressedData_out;

_CORBA_MODULE_VAR _dyn_attr const ::CORBA::TypeCode_ptr _tc_CompressedData;

_CORBA_MODULE_VAR _dyn_attr const ::CORBA::TypeCode_ptr _tc_CompressionEnablingPolicyValue;

typedef ::CORBA::Boolean CompressionEnablingPolicyValue;
typedef ::CORBA::Boolean_out CompressionEnablingPolicyValue_out;

_CORBA_MODULE_VAR _dyn_attr const ::CORBA::TypeCode_ptr _tc_CompressionIdLevelListPolicyValue;

typedef Compression::CompressorIdLevelList CompressionIdLevelListPolicyValue;
typedef Compression::CompressorIdLevelList_var CompressionIdLevelListPolicyValue_var;
typedef Compression::CompressorIdLevelList_out CompressionIdLevelListPolicyValue_out;

_CORBA_MODULE_VAR _dyn_attr const ::CORBA::TypeCode_ptr _tc_CompressionLowValuePolicyValue;

typedef ::CORBA::ULong CompressionLowValuePolicyValue;
typedef ::CORBA::ULong_out CompressionLowValuePolicyValue_out;

_CORBA_MODULE_VAR _dyn_attr const ::CORBA::TypeCode_ptr _tc_CompressionMinRatioPolicyValue;

typedef Compression::CompressionRatio CompressionMinRatioPolicyValue;
typedef Compression::CompressionRatio_out CompressionMinRatioPolicyValue_out;

_CORBA_MODULE_VARINT const ::CORBA::ULong COMPRESSION_ENABLING_POLICY_ID _init_in_decl_( = 64U );

_CORBA_MODULE_VARINT const ::CORBA::ULong COMPRESSOR_ID_LEVEL_LIST_POLICY_ID _init_in_decl_( = 65U );

_CORBA_MODULE_VARINT const ::CORBA::ULong COMPRESSION_LOW_VALUE_POLICY_ID _init_in_decl_( = 66U );

_CORBA_MODULE_VARINT const ::CORBA::ULong COMPRESSION_MIN_RATIO_POLICY_ID _init_in_decl_( = 67U );

#endif

