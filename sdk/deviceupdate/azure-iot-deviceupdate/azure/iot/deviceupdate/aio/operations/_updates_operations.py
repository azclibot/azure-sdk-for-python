# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models as _models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UpdatesOperations:
    """UpdatesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.iot.deviceupdate.models
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

    async def import_update(
        self,
        update_to_import: "_models.ImportUpdateInput",
        **kwargs
    ) -> None:
        """Import new update version.

        :param update_to_import: The update to be imported.
        :type update_to_import: ~azure.iot.deviceupdate.models.ImportUpdateInput
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
        action = "import"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.import_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
            'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['action'] = self._serialize.query("action", action, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(update_to_import, 'ImportUpdateInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    import_update.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates'}  # type: ignore

    async def get_update(
        self,
        provider: str,
        name: str,
        version: str,
        access_condition: Optional["_models.AccessCondition"] = None,
        **kwargs
    ) -> Optional["_models.Update"]:
        """Get a specific update version.

        :param provider: Update provider.
        :type provider: str
        :param name: Update name.
        :type name: str
        :param version: Update version.
        :type version: str
        :param access_condition: Parameter group.
        :type access_condition: ~azure.iot.deviceupdate.models.AccessCondition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Update, or the result of cls(response)
        :rtype: ~azure.iot.deviceupdate.models.Update or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.Update"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _if_none_match = None
        if access_condition is not None:
            _if_none_match = access_condition.if_none_match
        accept = "application/json"

        # Construct URL
        url = self.get_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
            'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
            'provider': self._serialize.url("provider", provider, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'version': self._serialize.url("version", version, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", _if_none_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Update', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_update.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers/{provider}/names/{name}/versions/{version}'}  # type: ignore

    async def delete_update(
        self,
        provider: str,
        name: str,
        version: str,
        **kwargs
    ) -> None:
        """Delete a specific update version.

        :param provider: Update provider.
        :type provider: str
        :param name: Update name.
        :type name: str
        :param version: Update version.
        :type version: str
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

        # Construct URL
        url = self.delete_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
            'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
            'provider': self._serialize.url("provider", provider, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'version': self._serialize.url("version", version, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
        response_headers['Operation-Location']=self._deserialize('str', response.headers.get('Operation-Location'))

        if cls:
            return cls(pipeline_response, None, response_headers)

    delete_update.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers/{provider}/names/{name}/versions/{version}'}  # type: ignore

    def get_providers(
        self,
        **kwargs
    ) -> AsyncIterable["_models.PageableListOfStrings"]:
        """Get a list of all update providers that have been imported to Device Update for IoT Hub.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PageableListOfStrings or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.iot.deviceupdate.models.PageableListOfStrings]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PageableListOfStrings"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_providers.metadata['url']  # type: ignore
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PageableListOfStrings', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_providers.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers'}  # type: ignore

    def get_names(
        self,
        provider: str,
        **kwargs
    ) -> AsyncIterable["_models.PageableListOfStrings"]:
        """Get a list of all update names that match the specified provider.

        :param provider: Update provider.
        :type provider: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PageableListOfStrings or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.iot.deviceupdate.models.PageableListOfStrings]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PageableListOfStrings"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_names.metadata['url']  # type: ignore
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                    'provider': self._serialize.url("provider", provider, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                    'provider': self._serialize.url("provider", provider, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PageableListOfStrings', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_names.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers/{provider}/names'}  # type: ignore

    def get_versions(
        self,
        provider: str,
        name: str,
        **kwargs
    ) -> AsyncIterable["_models.PageableListOfStrings"]:
        """Get a list of all update versions that match the specified provider and name.

        :param provider: Update provider.
        :type provider: str
        :param name: Update name.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PageableListOfStrings or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.iot.deviceupdate.models.PageableListOfStrings]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PageableListOfStrings"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_versions.metadata['url']  # type: ignore
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                    'provider': self._serialize.url("provider", provider, 'str'),
                    'name': self._serialize.url("name", name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                    'provider': self._serialize.url("provider", provider, 'str'),
                    'name': self._serialize.url("name", name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PageableListOfStrings', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_versions.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers/{provider}/names/{name}/versions'}  # type: ignore

    def get_files(
        self,
        provider: str,
        name: str,
        version: str,
        **kwargs
    ) -> AsyncIterable["_models.PageableListOfStrings"]:
        """Get a list of all update file identifiers for the specified version.

        :param provider: Update provider.
        :type provider: str
        :param name: Update name.
        :type name: str
        :param version: Update version.
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PageableListOfStrings or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.iot.deviceupdate.models.PageableListOfStrings]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PageableListOfStrings"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_files.metadata['url']  # type: ignore
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                    'provider': self._serialize.url("provider", provider, 'str'),
                    'name': self._serialize.url("name", name, 'str'),
                    'version': self._serialize.url("version", version, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                    'provider': self._serialize.url("provider", provider, 'str'),
                    'name': self._serialize.url("name", name, 'str'),
                    'version': self._serialize.url("version", version, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PageableListOfStrings', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_files.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers/{provider}/names/{name}/versions/{version}/files'}  # type: ignore

    async def get_file(
        self,
        provider: str,
        name: str,
        version: str,
        file_id: str,
        access_condition: Optional["_models.AccessCondition"] = None,
        **kwargs
    ) -> Optional["_models.File"]:
        """Get a specific update file from the version.

        :param provider: Update provider.
        :type provider: str
        :param name: Update name.
        :type name: str
        :param version: Update version.
        :type version: str
        :param file_id: File identifier.
        :type file_id: str
        :param access_condition: Parameter group.
        :type access_condition: ~azure.iot.deviceupdate.models.AccessCondition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: File, or the result of cls(response)
        :rtype: ~azure.iot.deviceupdate.models.File or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.File"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _if_none_match = None
        if access_condition is not None:
            _if_none_match = access_condition.if_none_match
        accept = "application/json"

        # Construct URL
        url = self.get_file.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
            'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
            'provider': self._serialize.url("provider", provider, 'str'),
            'name': self._serialize.url("name", name, 'str'),
            'version': self._serialize.url("version", version, 'str'),
            'fileId': self._serialize.url("file_id", file_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", _if_none_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('File', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_file.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/providers/{provider}/names/{name}/versions/{version}/files/{fileId}'}  # type: ignore

    def get_operations(
        self,
        filter: Optional[str] = None,
        top: Optional[int] = None,
        **kwargs
    ) -> AsyncIterable["_models.PageableListOfOperations"]:
        """Get a list of all import update operations. Completed operations are kept for 7 days before
        auto-deleted. Delete operations are not returned by this API version.

        :param filter: Restricts the set of operations returned. Only one specific filter is supported:
         "status eq 'NotStarted' or status eq 'Running'".
        :type filter: str
        :param top: Specifies a non-negative integer n that limits the number of items returned from a
         collection. The service returns the number of available items up to but not greater than the
         specified value n.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either PageableListOfOperations or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.iot.deviceupdate.models.PageableListOfOperations]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.PageableListOfOperations"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.get_operations.metadata['url']  # type: ignore
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
                if top is not None:
                    query_parameters['$top'] = self._serialize.query("top", top, 'int')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                path_format_arguments = {
                    'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
                    'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
                }
                url = self._client.format_url(url, **path_format_arguments)
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('PageableListOfOperations', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    get_operations.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/operations'}  # type: ignore

    async def get_operation(
        self,
        operation_id: str,
        access_condition: Optional["_models.AccessCondition"] = None,
        **kwargs
    ) -> Optional["_models.Operation"]:
        """Retrieve operation status.

        :param operation_id: Operation identifier.
        :type operation_id: str
        :param access_condition: Parameter group.
        :type access_condition: ~azure.iot.deviceupdate.models.AccessCondition
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Operation, or the result of cls(response)
        :rtype: ~azure.iot.deviceupdate.models.Operation or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.Operation"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        
        _if_none_match = None
        if access_condition is not None:
            _if_none_match = access_condition.if_none_match
        accept = "application/json"

        # Construct URL
        url = self.get_operation.metadata['url']  # type: ignore
        path_format_arguments = {
            'accountEndpoint': self._serialize.url("self._config.account_endpoint", self._config.account_endpoint, 'str', skip_quote=True),
            'instanceId': self._serialize.url("self._config.instance_id", self._config.instance_id, 'str', skip_quote=True),
            'operationId': self._serialize.url("operation_id", operation_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if _if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", _if_none_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        deserialized = None
        if response.status_code == 200:
            response_headers['Retry-After']=self._deserialize('str', response.headers.get('Retry-After'))
            deserialized = self._deserialize('Operation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized
    get_operation.metadata = {'url': '/deviceupdate/{instanceId}/v2/updates/operations/{operationId}'}  # type: ignore