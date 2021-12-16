# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Association(msrest.serialization.Model):
    """The resource definition of this association.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The association id.
    :vartype id: str
    :ivar name: The association name.
    :vartype name: str
    :ivar type: The association type.
    :vartype type: str
    :ivar target_resource_id: The REST resource instance of the target resource for this
     association.
    :vartype target_resource_id: str
    :ivar provisioning_state: The provisioning state of the association. Possible values include:
     "Accepted", "Deleting", "Running", "Succeeded", "Failed".
    :vartype provisioning_state: str or ~azure.mgmt.customproviders.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'target_resource_id': {'key': 'properties.targetResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword target_resource_id: The REST resource instance of the target resource for this
         association.
        :paramtype target_resource_id: str
        """
        super(Association, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.target_resource_id = kwargs.get('target_resource_id', None)
        self.provisioning_state = None


class AssociationsList(msrest.serialization.Model):
    """List of associations.

    :ivar value: The array of associations.
    :vartype value: list[~azure.mgmt.customproviders.models.Association]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Association]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword value: The array of associations.
        :paramtype value: list[~azure.mgmt.customproviders.models.Association]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super(AssociationsList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class CustomRPRouteDefinition(msrest.serialization.Model):
    """A route definition that defines an action or resource that can be interacted with through the custom resource provider.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the route definition. This becomes the name for the ARM
     extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
    :vartype name: str
    :ivar endpoint: Required. The route definition endpoint URI that the custom resource provider
     will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or
     can specify to route via a path (e.g. 'https://testendpoint/{requestPath}').
    :vartype endpoint: str
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the route definition. This becomes the name for the ARM
         extension (e.g.
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
        :paramtype name: str
        :keyword endpoint: Required. The route definition endpoint URI that the custom resource
         provider will proxy requests to. This can be in the form of a flat URI (e.g.
         'https://testendpoint/') or can specify to route via a path (e.g.
         'https://testendpoint/{requestPath}').
        :paramtype endpoint: str
        """
        super(CustomRPRouteDefinition, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.endpoint = kwargs['endpoint']


class CustomRPActionRouteDefinition(CustomRPRouteDefinition):
    """The route definition for an action implemented by the custom resource provider.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the route definition. This becomes the name for the ARM
     extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
    :vartype name: str
    :ivar endpoint: Required. The route definition endpoint URI that the custom resource provider
     will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or
     can specify to route via a path (e.g. 'https://testendpoint/{requestPath}').
    :vartype endpoint: str
    :ivar routing_type: The routing types that are supported for action requests. Possible values
     include: "Proxy".
    :vartype routing_type: str or ~azure.mgmt.customproviders.models.ActionRouting
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'routing_type': {'key': 'routingType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the route definition. This becomes the name for the ARM
         extension (e.g.
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
        :paramtype name: str
        :keyword endpoint: Required. The route definition endpoint URI that the custom resource
         provider will proxy requests to. This can be in the form of a flat URI (e.g.
         'https://testendpoint/') or can specify to route via a path (e.g.
         'https://testendpoint/{requestPath}').
        :paramtype endpoint: str
        :keyword routing_type: The routing types that are supported for action requests. Possible
         values include: "Proxy".
        :paramtype routing_type: str or ~azure.mgmt.customproviders.models.ActionRouting
        """
        super(CustomRPActionRouteDefinition, self).__init__(**kwargs)
        self.routing_type = kwargs.get('routing_type', None)


class Resource(msrest.serialization.Model):
    """The resource definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Required. Resource location.
    :vartype location: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword location: Required. Resource location.
        :paramtype location: str
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)


class CustomRPManifest(Resource):
    """A manifest file that defines the custom resource provider resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar location: Required. Resource location.
    :vartype location: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar actions: A list of actions that the custom resource provider implements.
    :vartype actions: list[~azure.mgmt.customproviders.models.CustomRPActionRouteDefinition]
    :ivar resource_types: A list of resource types that the custom resource provider implements.
    :vartype resource_types:
     list[~azure.mgmt.customproviders.models.CustomRPResourceTypeRouteDefinition]
    :ivar validations: A list of validations to run on the custom resource provider's requests.
    :vartype validations: list[~azure.mgmt.customproviders.models.CustomRPValidations]
    :ivar provisioning_state: The provisioning state of the resource provider. Possible values
     include: "Accepted", "Deleting", "Running", "Succeeded", "Failed".
    :vartype provisioning_state: str or ~azure.mgmt.customproviders.models.ProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'actions': {'key': 'properties.actions', 'type': '[CustomRPActionRouteDefinition]'},
        'resource_types': {'key': 'properties.resourceTypes', 'type': '[CustomRPResourceTypeRouteDefinition]'},
        'validations': {'key': 'properties.validations', 'type': '[CustomRPValidations]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword location: Required. Resource location.
        :paramtype location: str
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword actions: A list of actions that the custom resource provider implements.
        :paramtype actions: list[~azure.mgmt.customproviders.models.CustomRPActionRouteDefinition]
        :keyword resource_types: A list of resource types that the custom resource provider implements.
        :paramtype resource_types:
         list[~azure.mgmt.customproviders.models.CustomRPResourceTypeRouteDefinition]
        :keyword validations: A list of validations to run on the custom resource provider's requests.
        :paramtype validations: list[~azure.mgmt.customproviders.models.CustomRPValidations]
        """
        super(CustomRPManifest, self).__init__(**kwargs)
        self.actions = kwargs.get('actions', None)
        self.resource_types = kwargs.get('resource_types', None)
        self.validations = kwargs.get('validations', None)
        self.provisioning_state = None


class CustomRPResourceTypeRouteDefinition(CustomRPRouteDefinition):
    """The route definition for a resource implemented by the custom resource provider.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the route definition. This becomes the name for the ARM
     extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
    :vartype name: str
    :ivar endpoint: Required. The route definition endpoint URI that the custom resource provider
     will proxy requests to. This can be in the form of a flat URI (e.g. 'https://testendpoint/') or
     can specify to route via a path (e.g. 'https://testendpoint/{requestPath}').
    :vartype endpoint: str
    :ivar routing_type: The routing types that are supported for resource requests. Possible values
     include: "Proxy", "Proxy,Cache".
    :vartype routing_type: str or ~azure.mgmt.customproviders.models.ResourceTypeRouting
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'routing_type': {'key': 'routingType', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name: Required. The name of the route definition. This becomes the name for the ARM
         extension (e.g.
         '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}').
        :paramtype name: str
        :keyword endpoint: Required. The route definition endpoint URI that the custom resource
         provider will proxy requests to. This can be in the form of a flat URI (e.g.
         'https://testendpoint/') or can specify to route via a path (e.g.
         'https://testendpoint/{requestPath}').
        :paramtype endpoint: str
        :keyword routing_type: The routing types that are supported for resource requests. Possible
         values include: "Proxy", "Proxy,Cache".
        :paramtype routing_type: str or ~azure.mgmt.customproviders.models.ResourceTypeRouting
        """
        super(CustomRPResourceTypeRouteDefinition, self).__init__(**kwargs)
        self.routing_type = kwargs.get('routing_type', None)


class CustomRPValidations(msrest.serialization.Model):
    """A validation to apply on custom resource provider requests.

    All required parameters must be populated in order to send to Azure.

    :ivar validation_type: The type of validation to run against a matching request. Possible
     values include: "Swagger".
    :vartype validation_type: str or ~azure.mgmt.customproviders.models.ValidationType
    :ivar specification: Required. A link to the validation specification. The specification must
     be hosted on raw.githubusercontent.com.
    :vartype specification: str
    """

    _validation = {
        'specification': {'required': True, 'pattern': r'^https://raw.githubusercontent.com/.+'},
    }

    _attribute_map = {
        'validation_type': {'key': 'validationType', 'type': 'str'},
        'specification': {'key': 'specification', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword validation_type: The type of validation to run against a matching request. Possible
         values include: "Swagger".
        :paramtype validation_type: str or ~azure.mgmt.customproviders.models.ValidationType
        :keyword specification: Required. A link to the validation specification. The specification
         must be hosted on raw.githubusercontent.com.
        :paramtype specification: str
        """
        super(CustomRPValidations, self).__init__(**kwargs)
        self.validation_type = kwargs.get('validation_type', None)
        self.specification = kwargs['specification']


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar details: Internal error details.
    :vartype details: list[~azure.mgmt.customproviders.models.ErrorDefinition]
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.details = None


class ErrorResponse(msrest.serialization.Model):
    """Error response.

    :ivar error: The error details.
    :vartype error: ~azure.mgmt.customproviders.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword error: The error details.
        :paramtype error: ~azure.mgmt.customproviders.models.ErrorDefinition
        """
        super(ErrorResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class ListByCustomRPManifest(msrest.serialization.Model):
    """List of custom resource providers.

    :ivar value: The array of custom resource provider manifests.
    :vartype value: list[~azure.mgmt.customproviders.models.CustomRPManifest]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CustomRPManifest]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword value: The array of custom resource provider manifests.
        :paramtype value: list[~azure.mgmt.customproviders.models.CustomRPManifest]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super(ListByCustomRPManifest, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ResourceProviderOperation(msrest.serialization.Model):
    """Supported operations of this resource provider.

    :ivar name: Operation name, in format of {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: Display metadata associated with the operation.
    :vartype display: ~azure.mgmt.customproviders.models.ResourceProviderOperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'ResourceProviderOperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword name: Operation name, in format of {provider}/{resource}/{operation}.
        :paramtype name: str
        :keyword display: Display metadata associated with the operation.
        :paramtype display: ~azure.mgmt.customproviders.models.ResourceProviderOperationDisplay
        """
        super(ResourceProviderOperation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class ResourceProviderOperationDisplay(msrest.serialization.Model):
    """Display metadata associated with the operation.

    :ivar provider: Resource provider: Microsoft Custom Providers.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed.
    :vartype resource: str
    :ivar operation: Type of operation: get, read, delete, etc.
    :vartype operation: str
    :ivar description: Description of this operation.
    :vartype description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword provider: Resource provider: Microsoft Custom Providers.
        :paramtype provider: str
        :keyword resource: Resource on which the operation is performed.
        :paramtype resource: str
        :keyword operation: Type of operation: get, read, delete, etc.
        :paramtype operation: str
        :keyword description: Description of this operation.
        :paramtype description: str
        """
        super(ResourceProviderOperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class ResourceProviderOperationList(msrest.serialization.Model):
    """Results of the request to list operations.

    :ivar value: List of operations supported by this resource provider.
    :vartype value: list[~azure.mgmt.customproviders.models.ResourceProviderOperation]
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ResourceProviderOperation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword value: List of operations supported by this resource provider.
        :paramtype value: list[~azure.mgmt.customproviders.models.ResourceProviderOperation]
        :keyword next_link: The URL to use for getting the next set of results.
        :paramtype next_link: str
        """
        super(ResourceProviderOperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ResourceProvidersUpdate(msrest.serialization.Model):
    """custom resource provider update information.

    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        """
        super(ResourceProvidersUpdate, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
