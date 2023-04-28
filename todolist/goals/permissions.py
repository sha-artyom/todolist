from typing import Any

from rest_framework.permissions import (SAFE_METHODS, BasePermission,
                                        IsAuthenticated)
from rest_framework.request import Request

from todolist.goals.models import (Board, BoardParticipant, GoalCategory,
                                   GoalComment)


class BoardPermissions(IsAuthenticated):
    """Доступ к доске (разрешено только создателю)"""

    def has_object_permission(self, request: Request, view, board: Board) -> bool:
        _filters: dict[str: Any] = {'user_id': request.user.id, 'board_id': board.id}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**_filters).exists()


class GoalCategoryPermissions(IsAuthenticated):
    """Доступ к категории (разрешено только создателю)"""
    def has_object_permission(self, request: Request, view, goal_category: GoalCategory) -> bool:
        _filters: dict[str: Any] = {'user_id': request.user.id, 'board_id': goal_category.board_id}
        if request.method not in SAFE_METHODS:
            _filters['role'] = BoardParticipant.Role.owner

        return BoardParticipant.objects.filter(**_filters).exists()


class CommentPermissions(BasePermission):
    """Доступ к комментариям (действия разрешены только создателю, читателю отдает на просмотр)"""
    def has_object_permission(self, request: Request, view, comment: GoalComment) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return comment.user == request.user


class GoalPermissions(IsAuthenticated):
    """Доступ к цели (разрешено создателю и редактору)"""

    def has_object_permission(self, request: Request, view, obj) -> bool:
        if request.method in SAFE_METHODS:
            return BoardParticipant.objects.filter(user=request.user, board=obj.category.board).exists()

        return BoardParticipant.objects.filter(
            user=request.user,
            board=obj.category.board,
            role__in=[BoardParticipant.Role.owner, BoardParticipant.Role.writer]
        ).exists()
