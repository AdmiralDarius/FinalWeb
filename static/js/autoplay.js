$('.modal').on('shown.bs.modal',function (e) {
    let video =$(e.target).find("video")[0];
    if(video!==undefined){
        video.play();
    }
});
$('.modal').on('hide.bs.modal',function (e) {
  let video =$(e.target).find("video")[0];
    if(video!==undefined){
        video.pause();
    }
});