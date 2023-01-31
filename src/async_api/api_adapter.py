import aiohttp
import asyncio

class ExternalAPIdapter():

    def __init__(self, endpoints):
        self.endpoints = endpoints

    @staticmethod
    async def get_data(session, url):
        async with session.get(url) as resp:
            data = await resp.json()
            return data


    async def fetch(self):

        response_data = {}

        async with aiohttp.ClientSession() as session:

            tasks = []
            for endpoint in self.endpoints:
                url = endpoint
                tasks.append(asyncio.ensure_future(ExternalAPIdapter.get_data(session, url)))

            all_responses = await asyncio.gather(*tasks)
            for response in all_responses:
                if 'lastItemIndex' in response:
                    response_data['quotable_data'] = response['results']
                else:
                    response_data['randomuser_data'] = response['results']
            return response_data if response_data else {}        

