from ..validators import value_is_not_none_or_empty
from ..field import Field
from ..sensor import Sensor


class FB_DO_STB_S(Sensor):
    """
    Класс для работы с датчиками типа FB_DO_STB_S. Поле Severity отсутствует в таблице, его значение
    рассчитывается на основе значения в поле SOUND_ON.
    """

    BASE_TYPE = "Types.FB_DO_STB_S.FB_DO_STB_S_PLC"
    CLASS_NAME = "DO"
    Name = Field(name="name", column="D", validators=[value_is_not_none_or_empty])
    ColorOn = Field(name="ColorOn", column="Q", validators=[value_is_not_none_or_empty])
    GP = Field(name="GeneralPlan", column="J", validators=[value_is_not_none_or_empty])
    Description = Field(name="Description", column="E", validators=[value_is_not_none_or_empty])
    SirenType = Field(name="SirenType", column="N", validators=[value_is_not_none_or_empty])
    OxonTp = Field(name="OXON_TP", column="AE")

    def to_omx(self) -> str:
        omx_block = (
            f'    <ct:object {self.Name.name}="{getattr(self, self.Name.key)}" base-type="{self.BASE_TYPE}" aspect="Aspects.PLC" access-level="public" uuid="{self.pk}">\n'
            f'      <attribute type="Attributes.{self.GP.name}" value="{getattr(self, self.GP.key)}"/>\n'
            f'      <attribute type="Attributes.{self.ColorOn.name}" value="{getattr(self, self.ColorOn.key)}"/>\n'
            f'      <attribute type="unit.System.Attributes.{self.Description.name}" value="{getattr(self, self.Description.key)}"/>\n'
            f'      <attribute type="Attributes.{self.SirenType.name}" value="{getattr(self, self.SirenType.key)}"/>\n'
            f'      <attribute type="Attributes.{self.OxonTp.name}" value="{getattr(self, self.OxonTp.key)}"/>\n'
            f"    </ct:object>\n"
        )
        return omx_block

    def to_hmi(self, x: int, y: int) -> str:
        hmi_block = (
            f'    <object access-modifier="private" name="{getattr(self, self.Name.key)}" display-name="{getattr(self, self.Name.key)}" uuid="{self.pk}" base-type="FB_DO_STB_S" base-type-id="f9444f10-b26b-458a-9213-8247e191de57" ver="5" description="" cardinal="1">\n'
            f'        <designed target="X" value="{x}" ver="5"/>\n'
            f'        <designed target="Y" value="{y}" ver="5"/>\n'
            f'        <designed target="Rotation" value="0" ver="5"/>\n'
            f'        <init target="_init_Object" ver="5" value="KSPA001_SHU.{getattr(self, self.Name.key)}"/>\n'
            f"    </object>\n"
            f'    <object access-modifier="private" name="{getattr(self, self.Name.key)}" display-name="{getattr(self, self.Name.key)}" uuid="{self.tx}" base-type="Text" base-type-id="21d59f8d-2ca4-4592-92ca-b4dc48992a0f" ver="4">\n'
            f'        <designed target="X" value="{x+98}" ver="4"/>\n'
            f'        <designed target="Y" value="{y-45}" ver="4"/>\n'
            f'        <designed target="ZValue" value="0" ver="4"/>\n'
            f'        <designed target="Rotation" value="0" ver="4"/>\n'
            f'        <designed target="Scale" value="1" ver="4"/>\n'
            f'        <designed target="Visible" value="true" ver="4"/>\n'
            f'        <designed target="Opacity" value="1" ver="4"/>\n'
            f'        <designed target="Enabled" value="true" ver="4"/>\n'
            f'        <designed target="Tooltip" value="" ver="4"/>\n'
            f'        <designed target="Width" value="145.6667" ver="4"/>\n'
            f'        <designed target="Height" value="13.7143" ver="4"/>\n'
            f'        <designed target="Text" value="{getattr(self, self.Name.key)}" ver="4"/>\n'
            f'        <designed target="Font" value="Liberation Sans,10,-1,5,75,0,0,0,0,0,Bold" ver="4"/>\n'
            f'        <designed target="FontColor" value="0xff000000" ver="4"/>\n'
            f'        <designed target="TextAlignment" value="132" ver="4"/>\n'
            f"    </object>\n"
        )
        return hmi_block
