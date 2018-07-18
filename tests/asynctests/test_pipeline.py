#--------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#--------------------------------------------------------------------------
from msrest.pipeline import AsyncPipeline, ClientRequest
from msrest.pipeline.universal import UserAgentPolicy
from msrest.pipeline.aiohttp import AioHTTPSender
from msrest.pipeline.async_requests import AsyncBasicRequestsHTTPSender, AsyncRequestsHTTPSender

from msrest.configuration import Configuration

import pytest


@pytest.mark.asyncio
async def test_basic_aiohttp():

    request = ClientRequest("GET", "http://bing.com")
    policies = [
        UserAgentPolicy("myusergant")
    ]
    async with AsyncPipeline(policies) as pipeline:
        response = await pipeline.run(request)

    assert pipeline._sender._session.closed
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_basic_async_requests():

    request = ClientRequest("GET", "http://bing.com")
    policies = [
        UserAgentPolicy("myusergant")
    ]
    async with AsyncPipeline(policies, AsyncBasicRequestsHTTPSender()) as pipeline:
        response = await pipeline.run(request)

    assert response.status_code == 200

@pytest.mark.asyncio
async def test_conf_async_requests():

    conf = Configuration("http://bing.com/")
    request = ClientRequest("GET", "http://bing.com/")
    policies = [
        UserAgentPolicy("myusergant")
    ]
    async with AsyncPipeline(policies, AsyncRequestsHTTPSender(conf)) as pipeline:
        response = await pipeline.run(request)

    assert response.status_code == 200