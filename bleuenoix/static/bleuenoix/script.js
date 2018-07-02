$(document).ready(function () {

    $('#memeModal').on('show.bs.modal', function (e) {

      //get data-id attribute of the clicked element
      $("#modal-title").text($(e.relatedTarget).data('meme-title'));
      //populate the textboxe.currentTarget).find('#inside').val($(e.relatedTarget).data('meme-id'));
      $("#img-modal").attr("src", $(e.relatedTarget).data('meme-url'));
      $(".vote-button").attr("data-meme-id", $(e.relatedTarget).data('meme-id'));
      $('#number-upvotes').text($(e.relatedTarget).data('meme-upvotes'));
      $('#number-downvotes').text($(e.relatedTarget).data('meme-downvotes'));
      $('#meme-uploader').text($(e.relatedTarget).data('meme-uploader'));
      $('#edit-button').attr("href", "updatememe/"+ $(e.relatedTarget).data('meme-id'));
     
      if($(e.relatedTarget).data('meme-editable') == true)
      {
        $('#edit-button').show();
      }
      else
      {
        $('#edit-button').hide();
      }
      $('.vote-button').unbind();
      $(".vote-button").click({memeid: $(e.relatedTarget).data('meme-id')}, votefunction);
    
    });
  
    function votefunction (event) {
      var memeid = event.data.memeid;

      var appreciation = $(this).data('appreciation');
      $.ajax(
        {
          type: "GET",
          url: "/memes/" + appreciation + "meme",
          data: {
            post_id: memeid
          },
          success: function (data) {
            if (data.ok === false) {
              alert("Fail" + appreciation);
              return;
            }
            $('#number-upvotes').text(data.upvotes);
            $('#number-downvotes').text(data.downvotes);

            $("[data-meme-id="+memeid+"]").data("meme-upvotes",data.upvotes);
            $("[data-meme-id="+memeid+"]").data("meme-downvotes",data.downvotes);
   
          }
        })
    }
      

 
  });