using DAO.Model;
using Model.BoardRoom;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace DAO.Services.BoardRoom
{
    public class BoardRoomService : IBoardRoomService
    {
        private readonly HttpClient _httpClient;
        public BoardRoomService(HttpClient httpClient)
        {
            _httpClient = httpClient ?? throw new ArgumentNullException(nameof(httpClient));
        }

        public async Task<List<Protocol>> GetProtocols()
        {
            HttpResponseMessage httpResponseMessage = await _httpClient.GetAsync("protocols");
            string response = await httpResponseMessage.Content.ReadAsStringAsync();
            Response<Protocol> protocol = JsonSerializer.Deserialize<Response<Protocol>>(response, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
            return protocol.Data;
        }

        public async Task<List<Proposal>> GetProposals(string protocol)
        {
            HttpResponseMessage httpResponseMessage = await _httpClient.GetAsync($"protocols/{protocol}/proposals");
            string response = await httpResponseMessage.Content.ReadAsStringAsync();
            Response<Proposal> proposals = JsonSerializer.Deserialize<Response<Proposal>>(response, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
            return proposals.Data;
        }

        public async Task<List<Vote>> GetVotesOnProposals(string refId)
        {
            HttpResponseMessage httpResponseMessage = await _httpClient.GetAsync($"proposals/{refId}/votes");
            string response = await httpResponseMessage.Content.ReadAsStringAsync();
            Response<Vote> votes = JsonSerializer.Deserialize<Response<Vote>>(response, new JsonSerializerOptions { PropertyNameCaseInsensitive = true });
            return votes.Data;
        }
    }
}
