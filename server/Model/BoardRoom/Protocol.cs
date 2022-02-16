using System.Collections.Generic;
using System.Text.Json.Serialization;

namespace Model.BoardRoom
{
    public class Protocol
    {
        public string id { get; set; }
        public string Name { get; set; }
        public string CName { get; set; }
        public int TotalProposals { get; set; }
        public int TotalVotes { get; set; }
        public int UniqueVoters { get; set; }
        public List<Tokens> Tokens { get; set; }
        public List<Icons> Icons { get; set; }
        public DocumentType DocumentType { get; set; } = DocumentType.Protocol;
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
