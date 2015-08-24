/**
 * felix.shaw@tgac.ac.uk - 20/08/15.
 */

$(document).ready(function(){
    $('#search_box').keyup(function(e){
        search_elasticsearch(e)
    })
})

function search_elasticsearch(e){
    var searchterm = $('#search_box').val()
    $.ajax({
        type: "GET",
        url: "/rt_search_person",
        datatype: "json",
        data:{"firstname":searchterm, "lastname": searchterm},
        success: function(data){
            $('.suggestions').html('')
            data = jQuery.parseJSON(data)
            $(data.hits.hits).each(function(key, value){

                //console.log(value)
                $('.suggestions').append("<div>").append(value._source.firstname).append(' ').append(value._source.lastname).append('</div>')
            })

        },
        error: function(){
            alert('nup')
        }
    })
}

