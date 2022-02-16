using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace Model.BoardRoom
{
    public class Protocol
    {
        public string id { get; set; }
        public DocumentType DocumentType { get; set; } = DocumentType.Protocol;

        // Boardroom data
        public string Name { get; set; }
        public string CName { get; set; }
        public int TotalProposals { get; set; }
        public int TotalVotes { get; set; }
        public int UniqueVoters { get; set; }
        public List<Tokens> Tokens { get; set; }
        public List<Icons> Icons { get; set; }

        // Twitter Info
        public string TwitterHandle { get; set; }
        public string TwitterURL { get; set; }
        public string FollowerCount { get; set; }
        public string Category { get; set; }
    }

    public class Icons
    {
        public string Url { get; set; }
    }

    public class Tokens
    {
        public string Symbol { get; set; }
        public string Network { get; set; }
        public string ContractAddress { get; set; }
    }
}
