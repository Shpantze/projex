async function getItems(){
  let url = "/static/inapp/stuff.json";
  try{
    let res = await fetch(url);
    return await res.json();
  } catch(error){
    alert(error);
  }
}

async function renderItems(){
  let elems = await getItems();
  for(i of elems){
     let e = document.createTextNode(i.fields.item);
     let d = document.createElement("div");
      d.appendChild(e);
      document.body.appendChild(d);
  }
    
}
renderItems();

/*fetch('/static/inapp/tst.js')
   .then(response => response.text())
   .then(data => {
     let e = document.createTextNode(data)
     let d = document.createElement("div")
      d.appendChild(e)
      document.body.appendChild(d)
   })
   .catch(error => {
     alert(error);
   });
   */