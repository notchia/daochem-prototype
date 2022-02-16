using Model.BoardRoom;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace FrontEnd.Services.BoardRoom
{
    public interface IBackEndBoardRoomService
    {
        Task<List<Protocol>> GetProtocols();
        Task<List<Proposal>> GetProposals(string proposalName);
    }
}