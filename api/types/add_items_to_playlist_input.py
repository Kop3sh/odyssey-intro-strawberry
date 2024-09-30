import strawberry


@strawberry.input
class AddItemsToPlaylistInput:
    playlist_id: strawberry.ID
    uris: list[str]
