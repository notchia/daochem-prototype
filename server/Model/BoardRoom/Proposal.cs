using System.Collections.Generic;

namespace Model.BoardRoom
{
    public class Proposal
    {
        public string id { get; set; }
        public string RefId { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }
        public string Protocol { get; set; }
        public string Proposer { get; set; }
        public long TotalVotes { get; set; }
        public ProposalDate StartTime { get; set; }
        public ProposalDate EndTime { get; set; }
        public string StartTimestamp { get; set; }
        public string EndTimestamp { get; set; }
        public string CurrentState { get; set; }
        public string[] Choices { get; set; }
        public List<Result> Results { get; set; }
        public List<EventInformation> Events { get; set; }
        public DocumentType DocumentType = DocumentType.Proposal;
    }

    public class ProposalDate
    {
        public long BlockNumber { get; set; }
    }

    public class Result
    {
        public decimal Total { get; set; }
        public int Choice { get; set; }
    }

    public class EventInformation
    {
        public ProposalDate Time { get; set; }
        public string Event { get; set; }
        public long Timestamp { get; set; }
    }
}
