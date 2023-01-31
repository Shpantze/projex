var test = JSON.parse(document.getElementById("test").textContent);
var div = document.createElement("div");
document.body.appendChild(div);
for(i of test){ 
  for([key, value] of Object.entries(i)){
     var item = document.createTextNode(value);
   }
     var span = document.createElement("span");
     span.appendChild(item);
     div.appendChild(span);
     span.insertAdjacentHTML('afterend', '<br />');
}
var el = document.querySelectorAll('span');
for(j of el){
  j.addEventListener('click', function(e){
    if(!this.innerText.includes("X", 0)){
    this.insertAdjacentText('afterbegin', 'X');
    } else {
      this.innerText = this.innerText.substr(1);
    }
  })
}

