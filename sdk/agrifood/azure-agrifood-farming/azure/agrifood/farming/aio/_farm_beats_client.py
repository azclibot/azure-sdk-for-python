# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core import AsyncPipelineClient
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import FarmBeatsClientConfiguration
from .operations import ApplicationDataOperations
from .operations import AttachmentsOperations
from .operations import BoundariesOperations
from .operations import CropsOperations
from .operations import CropVarietiesOperations
from .operations import FarmersOperations
from .operations import FarmOperationsOperations
from .operations import FarmsOperations
from .operations import FieldsOperations
from .operations import HarvestDataOperations
from .operations import ImageProcessingOperations
from .operations import OAuthProvidersOperations
from .operations import OAuthTokensOperations
from .operations import PlantingDataOperations
from .operations import ScenesOperations
from .operations import SeasonalFieldsOperations
from .operations import SeasonsOperations
from .operations import TillageDataOperations
from .operations import WeatherOperations
from .. import models


class FarmBeatsClient(object):
    """APIs documentation for Azure AgPlatform DataPlane Service.

    :ivar application_data: ApplicationDataOperations operations
    :vartype application_data: azure.agrifood.farming.aio.operations.ApplicationDataOperations
    :ivar attachments: AttachmentsOperations operations
    :vartype attachments: azure.agrifood.farming.aio.operations.AttachmentsOperations
    :ivar boundaries: BoundariesOperations operations
    :vartype boundaries: azure.agrifood.farming.aio.operations.BoundariesOperations
    :ivar crops: CropsOperations operations
    :vartype crops: azure.agrifood.farming.aio.operations.CropsOperations
    :ivar crop_varieties: CropVarietiesOperations operations
    :vartype crop_varieties: azure.agrifood.farming.aio.operations.CropVarietiesOperations
    :ivar farmers: FarmersOperations operations
    :vartype farmers: azure.agrifood.farming.aio.operations.FarmersOperations
    :ivar farm_operations: FarmOperationsOperations operations
    :vartype farm_operations: azure.agrifood.farming.aio.operations.FarmOperationsOperations
    :ivar farms: FarmsOperations operations
    :vartype farms: azure.agrifood.farming.aio.operations.FarmsOperations
    :ivar fields: FieldsOperations operations
    :vartype fields: azure.agrifood.farming.aio.operations.FieldsOperations
    :ivar harvest_data: HarvestDataOperations operations
    :vartype harvest_data: azure.agrifood.farming.aio.operations.HarvestDataOperations
    :ivar image_processing: ImageProcessingOperations operations
    :vartype image_processing: azure.agrifood.farming.aio.operations.ImageProcessingOperations
    :ivar oauth_providers: OAuthProvidersOperations operations
    :vartype oauth_providers: azure.agrifood.farming.aio.operations.OAuthProvidersOperations
    :ivar oauth_tokens: OAuthTokensOperations operations
    :vartype oauth_tokens: azure.agrifood.farming.aio.operations.OAuthTokensOperations
    :ivar planting_data: PlantingDataOperations operations
    :vartype planting_data: azure.agrifood.farming.aio.operations.PlantingDataOperations
    :ivar scenes: ScenesOperations operations
    :vartype scenes: azure.agrifood.farming.aio.operations.ScenesOperations
    :ivar seasonal_fields: SeasonalFieldsOperations operations
    :vartype seasonal_fields: azure.agrifood.farming.aio.operations.SeasonalFieldsOperations
    :ivar seasons: SeasonsOperations operations
    :vartype seasons: azure.agrifood.farming.aio.operations.SeasonsOperations
    :ivar tillage_data: TillageDataOperations operations
    :vartype tillage_data: azure.agrifood.farming.aio.operations.TillageDataOperations
    :ivar weather: WeatherOperations operations
    :vartype weather: azure.agrifood.farming.aio.operations.WeatherOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param endpoint: The endpoint of your FarmBeats resource (protocol and hostname, for example: https://{resourceName}.farmbeats.azure.net).
    :type endpoint: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        endpoint: str,
        **kwargs: Any
    ) -> None:
        base_url = '{Endpoint}'
        self._config = FarmBeatsClientConfiguration(credential, endpoint, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.application_data = ApplicationDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.attachments = AttachmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.boundaries = BoundariesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.crops = CropsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.crop_varieties = CropVarietiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.farmers = FarmersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.farm_operations = FarmOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.farms = FarmsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.fields = FieldsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.harvest_data = HarvestDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.image_processing = ImageProcessingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.oauth_providers = OAuthProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.oauth_tokens = OAuthTokensOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planting_data = PlantingDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.scenes = ScenesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.seasonal_fields = SeasonalFieldsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.seasons = SeasonsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.tillage_data = TillageDataOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.weather = WeatherOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def _send_request(self, http_request: HttpRequest, **kwargs: Any) -> AsyncHttpResponse:
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.AsyncHttpResponse
        """
        path_format_arguments = {
            'Endpoint': self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = await self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "FarmBeatsClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
