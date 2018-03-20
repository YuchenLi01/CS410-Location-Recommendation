const serverURL = "http://localhost:5000/"

let get = (key, requestStr) => {
  return fetch(serverURL + key + '?' + requestStr, {
    method: 'GET',
    headers: {
      // 'Content-Type': 'application/json',
    },
  }).then(res => res.json());
}

let Api = {
  query(words) {
    let queryObj = {
      words: words
    };
    return get('', "words=" + JSON.stringify(queryObj));
  }
}

export default Api;