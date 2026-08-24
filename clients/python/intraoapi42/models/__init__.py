"""Contains all the data models used in inputs/outputs"""

from .achievement import Achievement
from .campus import Campus
from .campus_user import CampusUser
from .community_service import CommunityService
from .cursus import Cursus
from .cursus_user import CursusUser
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
from .group import Group
from .internship import Internship
from .internship_convention import InternshipConvention
from .internship_convention_convention import InternshipConventionConvention
from .language import Language
from .language_user import LanguageUser
from .light_accreditation import LightAccreditation
from .light_achievements_user import LightAchievementsUser
from .light_app import LightApp
from .light_campus import LightCampus
from .light_close import LightClose
from .light_coalition import LightCoalition
from .light_community_service import LightCommunityService
from .light_project import LightProject
from .light_team import LightTeam
from .light_team_user import LightTeamUser
from .light_user import LightUser
from .light_user_kind import LightUserKind
from .patch_project_user_by_id_body import PatchProjectUserByIdBody
from .patch_team_by_id_body import PatchTeamByIdBody
from .patronage import Patronage
from .post_projects_users_body import PostProjectsUsersBody
from .project_user import ProjectUser
from .project_user_create import ProjectUserCreate
from .project_user_update import ProjectUserUpdate
from .put_project_user_by_id_body import PutProjectUserByIdBody
from .put_team_by_id_body import PutTeamByIdBody
from .question_answer import QuestionAnswer
from .question_with_answers import QuestionWithAnswers
from .role import Role
from .scale_flag import ScaleFlag
from .scale_team import ScaleTeam
from .scale_team_truant import ScaleTeamTruant
from .scale_user import ScaleUser
from .skill import Skill
from .team import Team
from .team_update import TeamUpdate
from .team_update_teams_users_attributes_type_0_item import TeamUpdateTeamsUsersAttributesType0Item
from .team_upload import TeamUpload
from .title import Title
from .title_user import TitleUser
from .user import User
from .user_candidature import UserCandidature
from .user_candidature_gender import UserCandidatureGender
from .user_image import UserImage
from .user_image_versions import UserImageVersions

__all__ = (
    "Achievement",
    "Campus",
    "CampusUser",
    "CommunityService",
    "Cursus",
    "CursusUser",
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
    "Group",
    "Internship",
    "InternshipConvention",
    "InternshipConventionConvention",
    "Language",
    "LanguageUser",
    "LightAccreditation",
    "LightAchievementsUser",
    "LightApp",
    "LightCampus",
    "LightClose",
    "LightCoalition",
    "LightCommunityService",
    "LightProject",
    "LightTeam",
    "LightTeamUser",
    "LightUser",
    "LightUserKind",
    "PatchProjectUserByIdBody",
    "PatchTeamByIdBody",
    "Patronage",
    "PostProjectsUsersBody",
    "ProjectUser",
    "ProjectUserCreate",
    "ProjectUserUpdate",
    "PutProjectUserByIdBody",
    "PutTeamByIdBody",
    "QuestionAnswer",
    "QuestionWithAnswers",
    "Role",
    "ScaleFlag",
    "ScaleTeam",
    "ScaleTeamTruant",
    "ScaleUser",
    "Skill",
    "Team",
    "TeamUpdate",
    "TeamUpdateTeamsUsersAttributesType0Item",
    "TeamUpload",
    "Title",
    "TitleUser",
    "User",
    "UserCandidature",
    "UserCandidatureGender",
    "UserImage",
    "UserImageVersions",
)
