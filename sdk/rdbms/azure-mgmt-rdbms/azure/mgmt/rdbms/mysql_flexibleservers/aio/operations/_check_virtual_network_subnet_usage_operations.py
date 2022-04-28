# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._check_virtual_network_subnet_usage_operations import build_execute_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class CheckVirtualNetworkSubnetUsageOperations:
    """CheckVirtualNetworkSubnetUsageOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.rdbms.mysql_flexibleservers.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def execute(
        self,
        location_name: str,
        parameters: "_models.VirtualNetworkSubnetUsageParameter",
        **kwargs: Any
    ) -> "_models.VirtualNetworkSubnetUsageResult":
        """Get virtual network subnet usage for a given vNet resource id.

        :param location_name: The name of the location.
        :type location_name: str
        :param parameters: The required parameters for creating or updating a server.
        :type parameters:
         ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageParameter
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualNetworkSubnetUsageResult, or the result of cls(response)
        :rtype: ~azure.mgmt.rdbms.mysql_flexibleservers.models.VirtualNetworkSubnetUsageResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualNetworkSubnetUsageResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-05-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'VirtualNetworkSubnetUsageParameter')

        request = build_execute_request(
            subscription_id=self._config.subscription_id,
            location_name=location_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.execute.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VirtualNetworkSubnetUsageResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    execute.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.DBforMySQL/locations/{locationName}/checkVirtualNetworkSubnetUsage"}  # type: ignore

