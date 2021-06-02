# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class GlobalOperations(object):
    """GlobalOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.web.v2021_01_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_deleted_web_app(
        self,
        deleted_site_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DeletedSite"
        """Get deleted app for a subscription.

        Description for Get deleted app for a subscription.

        :param deleted_site_id: The numeric ID of the deleted app, e.g. 12345.
        :type deleted_site_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DeletedSite, or the result of cls(response)
        :rtype: ~azure.mgmt.web.v2021_01_01.models.DeletedSite
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.DeletedSite"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_deleted_web_app.metadata['url']  # type: ignore
        path_format_arguments = {
            'deletedSiteId': self._serialize.url("deleted_site_id", deleted_site_id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DeletedSite', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_deleted_web_app.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites/{deletedSiteId}'}  # type: ignore

    def get_deleted_web_app_snapshots(
        self,
        deleted_site_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> List["_models.Snapshot"]
        """Get all deleted apps for a subscription.

        Description for Get all deleted apps for a subscription.

        :param deleted_site_id: The numeric ID of the deleted app, e.g. 12345.
        :type deleted_site_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of Snapshot, or the result of cls(response)
        :rtype: list[~azure.mgmt.web.v2021_01_01.models.Snapshot]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.Snapshot"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_deleted_web_app_snapshots.metadata['url']  # type: ignore
        path_format_arguments = {
            'deletedSiteId': self._serialize.url("deleted_site_id", deleted_site_id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[Snapshot]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_deleted_web_app_snapshots.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/deletedSites/{deletedSiteId}/snapshots'}  # type: ignore

    def get_subscription_operation_with_async_response(
        self,
        location,  # type: str
        operation_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Gets an operation in a subscription and given region.

        Description for Gets an operation in a subscription and given region.

        :param location: Location name.
        :type location: str
        :param operation_id: Operation Id.
        :type operation_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2021-01-01"
        accept = "application/json"

        # Construct URL
        url = self.get_subscription_operation_with_async_response.metadata['url']  # type: ignore
        path_format_arguments = {
            'location': self._serialize.url("location", location, 'str'),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    get_subscription_operation_with_async_response.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/operations/{operationId}'}  # type: ignore
