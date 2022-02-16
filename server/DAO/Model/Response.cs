using System.Collections.Generic;

namespace DAO.Model
{
    public class Response<T>
    {
        public List<T> Data { get; set; }
    }
}
