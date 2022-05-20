# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class ProvisionState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Provision states for confluent RP
    """

    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETED = "Deleted"
    NOT_SPECIFIED = "NotSpecified"

class SaaSOfferStatus(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """SaaS Offer Status for confluent RP
    """

    STARTED = "Started"
    PENDING_FULFILLMENT_START = "PendingFulfillmentStart"
    IN_PROGRESS = "InProgress"
    SUBSCRIBED = "Subscribed"
    SUSPENDED = "Suspended"
    REINSTATED = "Reinstated"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    UNSUBSCRIBED = "Unsubscribed"
    UPDATING = "Updating"
