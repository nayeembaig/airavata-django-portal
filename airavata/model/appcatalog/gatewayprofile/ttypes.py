#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys
import airavata.model.appcatalog.computeresource.ttypes
import airavata.model.data.movement.ttypes
import airavata.model.appcatalog.accountprovisioning.ttypes

from thrift.transport import TTransport


class ComputeResourcePreference(object):
    """
    Gateway specific preferences for a Computer Resource

    computeResourceId:
      Corelate the preference to a compute resource.

    overridebyAiravata:
      If turned true, Airavata will override the preferences of better alternatives exist.

    loginUserName:
      If turned true, Airavata will override the preferences of better alternatives exist.

    preferredJobSubmissionProtocol:
      For resources with multiple job submission protocols, the gateway can pick a preferred option.

    preferredDataMovementProtocol:
      For resources with multiple data movement protocols, the gateway can pick a preferred option.

    preferredBatchQueue:
     Gateways can choose a defualt batch queue based on average job dimention, reservations or other metrics.

    scratchLocation:
     Path to the local scratch space on a HPC cluster. Typically used to create working directory for job execution.

    allocationProjectNumber:
     Typically used on HPC machines to charge computing usage to a account number. For instance, on XSEDE once an
       allocation is approved, an allocation number is assigned. Before passing this number with job submittions, the
       account to be used has to be added to the allocation.

    resourceSpecificCredentialStoreToken:
     Resource specific credential store token. If this token is specified, then it is superceeded by the gateway's
      default credential store.


    Attributes:
     - computeResourceId
     - overridebyAiravata
     - loginUserName
     - preferredJobSubmissionProtocol
     - preferredDataMovementProtocol
     - preferredBatchQueue
     - scratchLocation
     - allocationProjectNumber
     - resourceSpecificCredentialStoreToken
     - usageReportingGatewayId
     - qualityOfService
     - reservation
     - reservationStartTime
     - reservationEndTime
     - sshAccountProvisioner
     - sshAccountProvisionerConfig
     - sshAccountProvisionerAdditionalInfo
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'computeResourceId', 'UTF8', None, ),  # 1
        (2, TType.BOOL, 'overridebyAiravata', None, True, ),  # 2
        (3, TType.STRING, 'loginUserName', 'UTF8', None, ),  # 3
        (4, TType.I32, 'preferredJobSubmissionProtocol', None, None, ),  # 4
        (5, TType.I32, 'preferredDataMovementProtocol', None, None, ),  # 5
        (6, TType.STRING, 'preferredBatchQueue', 'UTF8', None, ),  # 6
        (7, TType.STRING, 'scratchLocation', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'allocationProjectNumber', 'UTF8', None, ),  # 8
        (9, TType.STRING, 'resourceSpecificCredentialStoreToken', 'UTF8', None, ),  # 9
        (10, TType.STRING, 'usageReportingGatewayId', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'qualityOfService', 'UTF8', None, ),  # 11
        (12, TType.STRING, 'reservation', 'UTF8', None, ),  # 12
        (13, TType.I64, 'reservationStartTime', None, None, ),  # 13
        (14, TType.I64, 'reservationEndTime', None, None, ),  # 14
        (15, TType.STRING, 'sshAccountProvisioner', 'UTF8', None, ),  # 15
        (16, TType.MAP, 'sshAccountProvisionerConfig', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 16
        (17, TType.STRING, 'sshAccountProvisionerAdditionalInfo', 'UTF8', None, ),  # 17
    )

    def __init__(self, computeResourceId=None, overridebyAiravata=thrift_spec[2][4], loginUserName=None, preferredJobSubmissionProtocol=None, preferredDataMovementProtocol=None, preferredBatchQueue=None, scratchLocation=None, allocationProjectNumber=None, resourceSpecificCredentialStoreToken=None, usageReportingGatewayId=None, qualityOfService=None, reservation=None, reservationStartTime=None, reservationEndTime=None, sshAccountProvisioner=None, sshAccountProvisionerConfig=None, sshAccountProvisionerAdditionalInfo=None,):
        self.computeResourceId = computeResourceId
        self.overridebyAiravata = overridebyAiravata
        self.loginUserName = loginUserName
        self.preferredJobSubmissionProtocol = preferredJobSubmissionProtocol
        self.preferredDataMovementProtocol = preferredDataMovementProtocol
        self.preferredBatchQueue = preferredBatchQueue
        self.scratchLocation = scratchLocation
        self.allocationProjectNumber = allocationProjectNumber
        self.resourceSpecificCredentialStoreToken = resourceSpecificCredentialStoreToken
        self.usageReportingGatewayId = usageReportingGatewayId
        self.qualityOfService = qualityOfService
        self.reservation = reservation
        self.reservationStartTime = reservationStartTime
        self.reservationEndTime = reservationEndTime
        self.sshAccountProvisioner = sshAccountProvisioner
        self.sshAccountProvisionerConfig = sshAccountProvisionerConfig
        self.sshAccountProvisionerAdditionalInfo = sshAccountProvisionerAdditionalInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.computeResourceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.overridebyAiravata = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.loginUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.preferredJobSubmissionProtocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.preferredDataMovementProtocol = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.preferredBatchQueue = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.scratchLocation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.allocationProjectNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.resourceSpecificCredentialStoreToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.usageReportingGatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.qualityOfService = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.reservation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I64:
                    self.reservationStartTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.reservationEndTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.STRING:
                    self.sshAccountProvisioner = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.MAP:
                    self.sshAccountProvisionerConfig = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.sshAccountProvisionerConfig[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.sshAccountProvisionerAdditionalInfo = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('ComputeResourcePreference')
        if self.computeResourceId is not None:
            oprot.writeFieldBegin('computeResourceId', TType.STRING, 1)
            oprot.writeString(self.computeResourceId.encode('utf-8') if sys.version_info[0] == 2 else self.computeResourceId)
            oprot.writeFieldEnd()
        if self.overridebyAiravata is not None:
            oprot.writeFieldBegin('overridebyAiravata', TType.BOOL, 2)
            oprot.writeBool(self.overridebyAiravata)
            oprot.writeFieldEnd()
        if self.loginUserName is not None:
            oprot.writeFieldBegin('loginUserName', TType.STRING, 3)
            oprot.writeString(self.loginUserName.encode('utf-8') if sys.version_info[0] == 2 else self.loginUserName)
            oprot.writeFieldEnd()
        if self.preferredJobSubmissionProtocol is not None:
            oprot.writeFieldBegin('preferredJobSubmissionProtocol', TType.I32, 4)
            oprot.writeI32(self.preferredJobSubmissionProtocol)
            oprot.writeFieldEnd()
        if self.preferredDataMovementProtocol is not None:
            oprot.writeFieldBegin('preferredDataMovementProtocol', TType.I32, 5)
            oprot.writeI32(self.preferredDataMovementProtocol)
            oprot.writeFieldEnd()
        if self.preferredBatchQueue is not None:
            oprot.writeFieldBegin('preferredBatchQueue', TType.STRING, 6)
            oprot.writeString(self.preferredBatchQueue.encode('utf-8') if sys.version_info[0] == 2 else self.preferredBatchQueue)
            oprot.writeFieldEnd()
        if self.scratchLocation is not None:
            oprot.writeFieldBegin('scratchLocation', TType.STRING, 7)
            oprot.writeString(self.scratchLocation.encode('utf-8') if sys.version_info[0] == 2 else self.scratchLocation)
            oprot.writeFieldEnd()
        if self.allocationProjectNumber is not None:
            oprot.writeFieldBegin('allocationProjectNumber', TType.STRING, 8)
            oprot.writeString(self.allocationProjectNumber.encode('utf-8') if sys.version_info[0] == 2 else self.allocationProjectNumber)
            oprot.writeFieldEnd()
        if self.resourceSpecificCredentialStoreToken is not None:
            oprot.writeFieldBegin('resourceSpecificCredentialStoreToken', TType.STRING, 9)
            oprot.writeString(self.resourceSpecificCredentialStoreToken.encode('utf-8') if sys.version_info[0] == 2 else self.resourceSpecificCredentialStoreToken)
            oprot.writeFieldEnd()
        if self.usageReportingGatewayId is not None:
            oprot.writeFieldBegin('usageReportingGatewayId', TType.STRING, 10)
            oprot.writeString(self.usageReportingGatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.usageReportingGatewayId)
            oprot.writeFieldEnd()
        if self.qualityOfService is not None:
            oprot.writeFieldBegin('qualityOfService', TType.STRING, 11)
            oprot.writeString(self.qualityOfService.encode('utf-8') if sys.version_info[0] == 2 else self.qualityOfService)
            oprot.writeFieldEnd()
        if self.reservation is not None:
            oprot.writeFieldBegin('reservation', TType.STRING, 12)
            oprot.writeString(self.reservation.encode('utf-8') if sys.version_info[0] == 2 else self.reservation)
            oprot.writeFieldEnd()
        if self.reservationStartTime is not None:
            oprot.writeFieldBegin('reservationStartTime', TType.I64, 13)
            oprot.writeI64(self.reservationStartTime)
            oprot.writeFieldEnd()
        if self.reservationEndTime is not None:
            oprot.writeFieldBegin('reservationEndTime', TType.I64, 14)
            oprot.writeI64(self.reservationEndTime)
            oprot.writeFieldEnd()
        if self.sshAccountProvisioner is not None:
            oprot.writeFieldBegin('sshAccountProvisioner', TType.STRING, 15)
            oprot.writeString(self.sshAccountProvisioner.encode('utf-8') if sys.version_info[0] == 2 else self.sshAccountProvisioner)
            oprot.writeFieldEnd()
        if self.sshAccountProvisionerConfig is not None:
            oprot.writeFieldBegin('sshAccountProvisionerConfig', TType.MAP, 16)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.sshAccountProvisionerConfig))
            for kiter7, viter8 in self.sshAccountProvisionerConfig.items():
                oprot.writeString(kiter7.encode('utf-8') if sys.version_info[0] == 2 else kiter7)
                oprot.writeString(viter8.encode('utf-8') if sys.version_info[0] == 2 else viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.sshAccountProvisionerAdditionalInfo is not None:
            oprot.writeFieldBegin('sshAccountProvisionerAdditionalInfo', TType.STRING, 17)
            oprot.writeString(self.sshAccountProvisionerAdditionalInfo.encode('utf-8') if sys.version_info[0] == 2 else self.sshAccountProvisionerAdditionalInfo)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.computeResourceId is None:
            raise TProtocolException(message='Required field computeResourceId is unset!')
        if self.overridebyAiravata is None:
            raise TProtocolException(message='Required field overridebyAiravata is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class StoragePreference(object):
    """
    Attributes:
     - storageResourceId
     - loginUserName
     - fileSystemRootLocation
     - resourceSpecificCredentialStoreToken
     - userStorageQuota
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'storageResourceId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'loginUserName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'fileSystemRootLocation', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'resourceSpecificCredentialStoreToken', 'UTF8', None, ),  # 4
        (5, TType.I64, 'userStorageQuota', None, None, ),  # 5
    )

    def __init__(self, storageResourceId=None, loginUserName=None, fileSystemRootLocation=None, resourceSpecificCredentialStoreToken=None, userStorageQuota=None,):
        self.storageResourceId = storageResourceId
        self.loginUserName = loginUserName
        self.fileSystemRootLocation = fileSystemRootLocation
        self.resourceSpecificCredentialStoreToken = resourceSpecificCredentialStoreToken
        self.userStorageQuota = userStorageQuota

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.storageResourceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.loginUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.fileSystemRootLocation = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.resourceSpecificCredentialStoreToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.userStorageQuota = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('StoragePreference')
        if self.storageResourceId is not None:
            oprot.writeFieldBegin('storageResourceId', TType.STRING, 1)
            oprot.writeString(self.storageResourceId.encode('utf-8') if sys.version_info[0] == 2 else self.storageResourceId)
            oprot.writeFieldEnd()
        if self.loginUserName is not None:
            oprot.writeFieldBegin('loginUserName', TType.STRING, 2)
            oprot.writeString(self.loginUserName.encode('utf-8') if sys.version_info[0] == 2 else self.loginUserName)
            oprot.writeFieldEnd()
        if self.fileSystemRootLocation is not None:
            oprot.writeFieldBegin('fileSystemRootLocation', TType.STRING, 3)
            oprot.writeString(self.fileSystemRootLocation.encode('utf-8') if sys.version_info[0] == 2 else self.fileSystemRootLocation)
            oprot.writeFieldEnd()
        if self.resourceSpecificCredentialStoreToken is not None:
            oprot.writeFieldBegin('resourceSpecificCredentialStoreToken', TType.STRING, 4)
            oprot.writeString(self.resourceSpecificCredentialStoreToken.encode('utf-8') if sys.version_info[0] == 2 else self.resourceSpecificCredentialStoreToken)
            oprot.writeFieldEnd()
        if self.userStorageQuota is not None:
            oprot.writeFieldBegin('userStorageQuota', TType.I64, 5)
            oprot.writeI64(self.userStorageQuota)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.storageResourceId is None:
            raise TProtocolException(message='Required field storageResourceId is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GatewayResourceProfile(object):
    """
    Gateway Resource Profile

    gatewayID:
     Unique identifier for the gateway assigned by Airavata. Corelate this to Airavata Admin API Gateway Registration.

    credentialStoreToken:
     Gateway's defualt credential store token.

    computeResourcePreferences:
     List of resource preferences for each of the registered compute resources.

     identityServerTenant:

     identityServerPwdCredToken:


    Attributes:
     - gatewayID
     - credentialStoreToken
     - computeResourcePreferences
     - storagePreferences
     - identityServerTenant
     - identityServerPwdCredToken
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'gatewayID', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'credentialStoreToken', 'UTF8', None, ),  # 2
        (3, TType.LIST, 'computeResourcePreferences', (TType.STRUCT, (ComputeResourcePreference, ComputeResourcePreference.thrift_spec), False), None, ),  # 3
        (4, TType.LIST, 'storagePreferences', (TType.STRUCT, (StoragePreference, StoragePreference.thrift_spec), False), None, ),  # 4
        (5, TType.STRING, 'identityServerTenant', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'identityServerPwdCredToken', 'UTF8', None, ),  # 6
    )

    def __init__(self, gatewayID=None, credentialStoreToken=None, computeResourcePreferences=None, storagePreferences=None, identityServerTenant=None, identityServerPwdCredToken=None,):
        self.gatewayID = gatewayID
        self.credentialStoreToken = credentialStoreToken
        self.computeResourcePreferences = computeResourcePreferences
        self.storagePreferences = storagePreferences
        self.identityServerTenant = identityServerTenant
        self.identityServerPwdCredToken = identityServerPwdCredToken

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.gatewayID = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.credentialStoreToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.computeResourcePreferences = []
                    (_etype12, _size9) = iprot.readListBegin()
                    for _i13 in range(_size9):
                        _elem14 = ComputeResourcePreference()
                        _elem14.read(iprot)
                        self.computeResourcePreferences.append(_elem14)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.storagePreferences = []
                    (_etype18, _size15) = iprot.readListBegin()
                    for _i19 in range(_size15):
                        _elem20 = StoragePreference()
                        _elem20.read(iprot)
                        self.storagePreferences.append(_elem20)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.identityServerTenant = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.identityServerPwdCredToken = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('GatewayResourceProfile')
        if self.gatewayID is not None:
            oprot.writeFieldBegin('gatewayID', TType.STRING, 1)
            oprot.writeString(self.gatewayID.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayID)
            oprot.writeFieldEnd()
        if self.credentialStoreToken is not None:
            oprot.writeFieldBegin('credentialStoreToken', TType.STRING, 2)
            oprot.writeString(self.credentialStoreToken.encode('utf-8') if sys.version_info[0] == 2 else self.credentialStoreToken)
            oprot.writeFieldEnd()
        if self.computeResourcePreferences is not None:
            oprot.writeFieldBegin('computeResourcePreferences', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.computeResourcePreferences))
            for iter21 in self.computeResourcePreferences:
                iter21.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.storagePreferences is not None:
            oprot.writeFieldBegin('storagePreferences', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.storagePreferences))
            for iter22 in self.storagePreferences:
                iter22.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.identityServerTenant is not None:
            oprot.writeFieldBegin('identityServerTenant', TType.STRING, 5)
            oprot.writeString(self.identityServerTenant.encode('utf-8') if sys.version_info[0] == 2 else self.identityServerTenant)
            oprot.writeFieldEnd()
        if self.identityServerPwdCredToken is not None:
            oprot.writeFieldBegin('identityServerPwdCredToken', TType.STRING, 6)
            oprot.writeString(self.identityServerPwdCredToken.encode('utf-8') if sys.version_info[0] == 2 else self.identityServerPwdCredToken)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.gatewayID is None:
            raise TProtocolException(message='Required field gatewayID is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
