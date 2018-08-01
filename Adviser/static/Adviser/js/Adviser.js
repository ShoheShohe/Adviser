// 入力フォームでリターンキー押下時に送信させない
$('#myform').on('sumbit', function (e) {
    e.preventDefault();
})

// 連続送信防止
$('.save').on('click', function (e) {
    $('.save').addClass('disabled');
    $('#myform').submit();
})

// listviewのcard上でレーティングした時に、ページをリロードさせない。これ使ったらsubmitできなくなってる。
$('#rating').on('submit', function(e) {
    //e.preventDefault();
})