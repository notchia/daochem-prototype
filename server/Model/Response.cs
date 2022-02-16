using System.Collections.Generic;

namespace Model
{
    public class Response<T>
    {
        public List<T> Data { get; set; }
    }
}
