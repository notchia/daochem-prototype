namespace Model.BoardRoom
{
    public class Vote
    {
        public string id { get; set; }
        public string RefId { get; set; }
        public string Protocol { get; set; }
        public string Address { get; set; }
        public decimal Power { get; set; }
        public int Choice { get; set; }
        public Time Time { get; set; }
        public string Timestamp { get; set; }
        public DocumentType DocumentType = DocumentType.Vote;
    }

    public class Time
    {
        public long BlockNumber { get; set; }
    }
}
