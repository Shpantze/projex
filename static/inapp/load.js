document.addEventListener("visibilitychange", () => {
  if(document.visibilityState === 'visible'){
    alert('welcome back!')
  }
});