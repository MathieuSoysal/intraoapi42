"""Contains all the data models used in inputs/outputs"""

from .achievement_response import AchievementResponse
from .campus_response import CampusResponse
from .campus_user_response import CampusUserResponse
from .close_response import CloseResponse
from .close_response_kind import CloseResponseKind
from .community_service_response import CommunityServiceResponse
from .cursus_response import CursusResponse
from .cursus_user_response import CursusUserResponse
from .error import Error
from .get_closes_by_user_id_filter import GetClosesByUserIdFilter
from .get_closes_by_user_id_range import GetClosesByUserIdRange
from .get_closes_by_user_id_sort import GetClosesByUserIdSort
from .get_closes_filter import GetClosesFilter
from .get_closes_range import GetClosesRange
from .get_closes_sort import GetClosesSort
from .get_internships_filter import GetInternshipsFilter
from .get_internships_range import GetInternshipsRange
from .get_projects_users_by_user_id_filter import GetProjectsUsersByUserIdFilter
from .get_projects_users_by_user_id_range import GetProjectsUsersByUserIdRange
from .get_users_filter import GetUsersFilter
from .get_users_range import GetUsersRange
from .group_response import GroupResponse
from .internship_response import InternshipResponse
from .internship_response_convention import InternshipResponseConvention
from .internship_response_convention_convention import InternshipResponseConventionConvention
from .language_response import LanguageResponse
from .language_user_response import LanguageUserResponse
from .light_project_response import LightProjectResponse
from .light_team_response import LightTeamResponse
from .light_user_response import LightUserResponse
from .light_user_response_kind import LightUserResponseKind
from .patch_project_user_by_id_body import PatchProjectUserByIdBody
from .patch_team_by_id_body import PatchTeamByIdBody
from .patronage_response import PatronageResponse
from .post_projects_users_body import PostProjectsUsersBody
from .project_user_create import ProjectUserCreate
from .project_user_response import ProjectUserResponse
from .project_user_update import ProjectUserUpdate
from .put_project_user_by_id_body import PutProjectUserByIdBody
from .put_team_by_id_body import PutTeamByIdBody
from .question_answer_response import QuestionAnswerResponse
from .question_with_answers_response import QuestionWithAnswersResponse
from .role_response import RoleResponse
from .scale_flag_response import ScaleFlagResponse
from .scale_team_response import ScaleTeamResponse
from .scale_team_response_truant import ScaleTeamResponseTruant
from .scale_user_response import ScaleUserResponse
from .skill_response import SkillResponse
from .team_response import TeamResponse
from .team_update import TeamUpdate
from .team_update_teams_users_attributes_type_0_item import TeamUpdateTeamsUsersAttributesType0Item
from .team_upload_response import TeamUploadResponse
from .team_user_response import TeamUserResponse
from .title_response import TitleResponse
from .title_user_response import TitleUserResponse
from .user_candidature_response import UserCandidatureResponse
from .user_candidature_response_gender import UserCandidatureResponseGender
from .user_image_response import UserImageResponse
from .user_image_response_versions import UserImageResponseVersions
from .user_response import UserResponse

__all__ = (
    "AchievementResponse",
    "CampusResponse",
    "CampusUserResponse",
    "CloseResponse",
    "CloseResponseKind",
    "CommunityServiceResponse",
    "CursusResponse",
    "CursusUserResponse",
    "Error",
    "GetClosesByUserIdFilter",
    "GetClosesByUserIdRange",
    "GetClosesByUserIdSort",
    "GetClosesFilter",
    "GetClosesRange",
    "GetClosesSort",
    "GetInternshipsFilter",
    "GetInternshipsRange",
    "GetProjectsUsersByUserIdFilter",
    "GetProjectsUsersByUserIdRange",
    "GetUsersFilter",
    "GetUsersRange",
    "GroupResponse",
    "InternshipResponse",
    "InternshipResponseConvention",
    "InternshipResponseConventionConvention",
    "LanguageResponse",
    "LanguageUserResponse",
    "LightProjectResponse",
    "LightTeamResponse",
    "LightUserResponse",
    "LightUserResponseKind",
    "PatchProjectUserByIdBody",
    "PatchTeamByIdBody",
    "PatronageResponse",
    "PostProjectsUsersBody",
    "ProjectUserCreate",
    "ProjectUserResponse",
    "ProjectUserUpdate",
    "PutProjectUserByIdBody",
    "PutTeamByIdBody",
    "QuestionAnswerResponse",
    "QuestionWithAnswersResponse",
    "RoleResponse",
    "ScaleFlagResponse",
    "ScaleTeamResponse",
    "ScaleTeamResponseTruant",
    "ScaleUserResponse",
    "SkillResponse",
    "TeamResponse",
    "TeamUpdate",
    "TeamUpdateTeamsUsersAttributesType0Item",
    "TeamUploadResponse",
    "TeamUserResponse",
    "TitleResponse",
    "TitleUserResponse",
    "UserCandidatureResponse",
    "UserCandidatureResponseGender",
    "UserImageResponse",
    "UserImageResponseVersions",
    "UserResponse",
)
