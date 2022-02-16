using DAO.Repository;
using DAO.Services.BoardRoom;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Model.BoardRoom;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DAO.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class BoardRoomController : ControllerBase
    {
        private readonly ILogger<BoardRoomController> _logger;
        private IBoardRoomService _boardRoomService;
        private IRepository _repository;
        public BoardRoomController(ILogger<BoardRoomController> logger, IBoardRoomService boardRoomService, IRepository repository)
        {
            _logger = logger ?? throw new Exception(nameof(logger));
            _boardRoomService = boardRoomService ?? throw new ArgumentNullException(nameof(boardRoomService));
            _repository = repository ?? throw new ArgumentNullException(nameof(repository));
        }

        [HttpGet("protocols")]
        public async Task<ActionResult<List<Protocol>>> GetProtocols()
        {
            try
            {
                var protocols = await _repository.GetProtocols();
                if (protocols is null || protocols.Count == 0)
                {
                    protocols = await _boardRoomService.GetProtocols();
                    foreach (var protocol in protocols)
                    {
                        await _repository.PostProtocols(protocol);
                    }
                }

                return protocols;
            } 
            catch (Exception ex)
            {
                _logger.LogError(ex, ex.Message);
                return StatusCode(500);
            }
        }

        [HttpGet("protocols/{protocolName}")]
        public async Task<ActionResult<List<Protocol>>> GetProtocols(string protocolName)
        {
            try
            {
                List<Protocol> protocols = await _repository.GetProtocols();
                return protocols.Where(protocol => protocol.Name.ToLower() == protocolName.ToLower()).ToList();
            } 
            catch (Exception ex)
            {
                _logger.LogError(ex, ex.Message);
                return StatusCode(500);
            }
        }

        [HttpGet("protocols/{protocolName}/proposals")]
        public async Task<ActionResult<List<Proposal>>> GetProposals(string protocolName)
        {
            try
            {
                if (string.IsNullOrEmpty(protocolName))
                    return BadRequest($"{nameof(protocolName)} can't be empty or null");
                var proposalsToReturn = new List<Proposal>();
                var proposals = await _repository.GetProposals();
                if (proposals is null || proposals.Count == 0)
                {
                    var protocols = await _repository.GetProtocols();
                    foreach (var protocol in protocols)
                    {
                        proposals = await _boardRoomService.GetProposals(protocol.CName);
                        if (proposals.Count != 0)
                        {
                            Console.WriteLine("*");
                        }
                        foreach (var proposal in proposals)
                        {
                            await _repository.PostProposal(proposal);
                        }
                    }
                }

                return Ok(proposals.Where(p => p.Protocol == protocolName).ToList());
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, ex.Message);
                return StatusCode(500);
            }
        }
        
        [HttpGet("protocols/proposals/{refId}/votes")]
        public async Task<ActionResult<List<Vote>>> GetProposalsVotes(string refId)
        {
            try
            {
                if (string.IsNullOrEmpty(refId))
                    return BadRequest($"{nameof(refId)} can't be empty or null");
                var votes = await _repository.GetVotes();
                if (votes is null || votes.Count == 0)
                {
                    votes = await _boardRoomService.GetVotesOnProposals(refId);
                    foreach (var vote in votes)
                    {
                        await _repository.PostVote(vote);
                    }
                }
                return Ok();
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, ex.Message);
                return StatusCode(500);
            }
        }
    }
}
