/* globals $ */

$('.fav-book').on('click', (event) => {
  event.preventDefault()
  const $button = $(event.currentTarget)
  const bookId = $button.data('book-id')
  const csrfToken = $button.siblings('[name=csrfmiddlewaretoken]').val()
  $.post(`/books/${bookId}/favorite/`, {
    'csrfmiddlewaretoken': csrfToken
  }, (data) => {
    if (data.favorite) {
      $button.html('&#x2605;')
    } else {
      $button.html('&#x2606;')
    }
  })
})
