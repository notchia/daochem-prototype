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
        // name,key_word_tweet_count,tweet_count,key_word_ratio,likes,follower_count,like_follower_ratio
        public long? key_word_tweet_count { get; set; }
        public long? tweet_count { get; set; }
        public decimal? key_word_ratio { get; set; }
        public long? likes { get; set; }
        public decimal? like_follower_ratio { get; set; }
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
