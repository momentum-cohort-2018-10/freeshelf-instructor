/* global $ */

console.log('JS running')

const FILLED_IN_STAR = '&#x2605;'
const EMPTY_STAR = '&#x2606;'

function pluralize (num, singular, plural) {
  if (plural === undefined) {
    plural = singular + 's'
  }

  return `${num} ${num === 1 ? singular : plural}`
}

$('.toggle-favorite-form').on('submit', function (event) {
  event.preventDefault()
  const csrfToken = $(event.target).find('[name=csrfmiddlewaretoken]').val()
  $.ajax({
    method: 'POST',
    url: event.target.action,
    data: {
      'csrfmiddlewaretoken': csrfToken
    },
    success: function (results) {
      let starToUse
      if (results.favorite) {
        starToUse = FILLED_IN_STAR
      } else {
        starToUse = EMPTY_STAR
      }
      $(event.target).find('button[type=submit]').html(starToUse)

      $(`#book-${results.book_id}`).find('.book-num-favorites').text(
        `Favorited ${pluralize(results.num_of_favorites, 'time')}`
      )
    }
  })
})
