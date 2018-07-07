
$(document).ready(function () {

  $.ajax(
    {
      type: "GET",
      url: "/memes/getAllMemes",
      data: {},
      success: function (data) {
        var memes = data.memes;
        $.each(memes, function (index, value) {
          var divWrapper = $("<div class ='container-overlay'>");
          var memeToAdd = $("<div>");
          var background = $("<div>", {
            "class": "center-cropped",
            "style": "background-image: url(" + value.image + ");"
          });
          memeToAdd.append(background);
          var aboveoverlay = $("<div>", {
            "data-meme-id": value.id,
            "data-meme-uploader": value.uploader,
            "data-meme-upvotes": value.upvoters,
            "data-meme-downvotes": value.downvoters,
            "data-meme-category": value.category,
            "data-meme-title": value.title,
            "data-meme-url": value.image,
            "data-meme-editable": value.editable,
            "data-meme-deletable": value.deletable,
            "class": "modal-opener above-overlay",
            "data-toggle": "modal",
            "data-target": "#memeModal"
          });
          var overlay = $("<div>", {
            "class": "overlay"
          });
          var buttonUpVote = $("<span>", {
            "class": "vote-button-overlay no-modal",
            "data-meme-id": value.id,
            "data-appreciation": "like"
          });
          buttonUpVote.html("👍");
          var buttonDownVote = $("<span>", {
            "class": "vote-button no-modal",
            "data-meme-id": value.id,
            "data-appreciation": "dislike"
          });

           buttonDownVote.html("👎");
           buttonUpVote.click({ memeid: value.id }, votefunction);

           buttonDownVote.click({ memeid: value.id }, votefunction);
      
          overlay.append(buttonUpVote);
          overlay.append(buttonDownVote);
          background.append(aboveoverlay);
          background.append(overlay);
          divWrapper.append(memeToAdd);
          $("#grid").append(divWrapper);


        });
        salvattore.rescanMediaQueries();
      }
    })

  $('#memeModal').on('show.bs.modal', function (e) {
    //get data-id attribute of the clicked element
    $("#modal-title").text($(e.relatedTarget).data('meme-title'));
    //populate the textboxe.currentTarget).find('#inside').val($(e.relatedTarget).data('meme-id'));
    $("#img-modal").attr("src", $(e.relatedTarget).data('meme-url'));
    $(".vote-button").attr("data-meme-id", $(e.relatedTarget).data('meme-id'));
    $('#number-upvotes').text($(e.relatedTarget).data('meme-upvotes'));
    $('#number-downvotes').text($(e.relatedTarget).data('meme-downvotes'));
    $('#meme-uploader').text($(e.relatedTarget).data('meme-uploader'));
    $('#meme-category').text($(e.relatedTarget).data('meme-category'));
    $('#edit-button').attr("href", "updatememe/" + $(e.relatedTarget).data('meme-id'));
    $('#delete-button').attr("href", "deletememe/" + $(e.relatedTarget).data('meme-id'));

    if ($(e.relatedTarget).data('meme-editable') === true) {
      $('#edit-button').show();
    }
    else {
      $('#edit-button').hide();
    }
    if ($(e.relatedTarget).data('meme-deletable') === true) {
      $('#delete-button').show();
    }
    else {
      $('#delete-button').hide();
    }
    $('.vote-button').unbind();
    $(".vote-button").click({ memeid: $(e.relatedTarget).data('meme-id') }, votefunction);
    $('#delete-button').click({ memeid: $(e.relatedTarget).data('meme-id') }, deletefunction);
  });
  function deletefunction(event) {
    var memeid = event.data.memeid;
    $.ajax(
      {
        type: "GET",
        url: "/memes/deletememe",
        data: {
          post_id: memeid
        },
        success: function (data) {
          if (data.ok === false) {
            alert("Fail");
            return;
          }
          $("[data-meme-id=" + memeid + "]").remove();
          salvattore.recreateColumns(document.querySelector('#grid'));
          $('#memeModal').modal('toggle');
        }
      })
  }
  function votefunction(event) {
    var memeid = event.data.memeid;
    var appreciation = $(this).data('appreciation');
    console.log(memeid);
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

          $("[data-meme-id=" + memeid + "]").data("meme-upvotes", data.upvotes);
          $("[data-meme-id=" + memeid + "]").data("meme-downvotes", data.downvotes);

        }
      })
  }



});