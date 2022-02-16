using Model.BoardRoom;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace FrontEnd.Services.BoardRoom
{
    public class BackEndBoardRoomService : IBackEndBoardRoomService
    {
        private readonly HttpClient _httpClient;
        public BackEndBoardRoomService(HttpClient httpClient)
        {
            _httpClient = httpClient ?? throw new ArgumentNullException(nameof(httpClient));
        }

        public async Task<List<Protocol>> GetProtocols()
        {
            HttpResponseMessage httpResponseMessage = await _httpClient.GetAsync("/api/boardroom/protocols");
            string response = await httpResponseMessage.Content.ReadAsStringAsync();
            List<Protocol> protocols = JsonSerializer.Deserialize<List<Protocol>>(response, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
            return protocols;
        }

        public async Task<List<Proposal>> GetProposals(string protocolName)
        {
            HttpResponseMessage httpResponseMessage = await _httpClient.GetAsync($"/api/boardroom/protocols/{protocolName}/proposals");
            string response = await httpResponseMessage.Content.ReadAsStringAsync();
            List<Proposal> proposals = JsonSerializer.Deserialize<List<Proposal>>(response, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
            return proposals;
        }
    }
}