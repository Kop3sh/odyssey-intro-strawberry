import strawberry

from mock_spotify_rest_api_client.api.playlists import (
    get_featured_playlists,
    get_playlist,
)

from .types.playlist import Playlist


@strawberry.type
class Query:

    @strawberry.field(description="Playlists hand-picked to be featured to all users.")
    async def featured_playlists(self, info: strawberry.Info) -> list[Playlist]:
        spotify_client = info.context["spotify_client"]
        data = await get_featured_playlists.asyncio(client=spotify_client)

        playlists = [
            Playlist(
                id=strawberry.ID(playlist.id),
                name=playlist.name,
                description=playlist.description,
            )
            for playlist in data.playlists.items
        ]
        return playlists

    @strawberry.field(description="Retrieves a specific playlist.")
    async def playlist(
        self,
        id: strawberry.ID,
        info: strawberry.Info,
    ) -> Playlist | None:
        spotify_client = info.context["spotify_client"]
        data = await get_playlist.asyncio(client=spotify_client, playlist_id=id)

        if data is None:
            return None

        return Playlist(
            id=strawberry.ID(data.id),
            name=data.name,
            description=data.description,
        )
