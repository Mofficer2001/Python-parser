from ..validators import value_is_not_none_or_empty
from ..field import Field
from ..sensor import Sensor


class FB_QSA_S(Sensor):
    """
    Класс для работы с датчиками типа FB_QSA_S. Поле Severity отсутствует в таблице, его значение
    рассчитывается на основе значения в поле SOUND_ON.
    """

    BASE_TYPE = "Types.FB_QSA_S.FB_QSA_S_PLC"
    CLASS_NAME = "QSA"
    Name = Field(name="name", column="D", validators=[value_is_not_none_or_empty])
    EUnit = Field(name="EUnit", column="L", validators=[value_is_not_none_or_empty])
    GP = Field(name="GeneralPlan", column="J", validators=[value_is_not_none_or_empty])
    Description = Field(name="Description", column="E", validators=[value_is_not_none_or_empty])
    IvxxTp = Field(name="IVXX_TP", column="Y")
    Substance = Field(name="Substance", column="N", validators=[value_is_not_none_or_empty])
    IfexTp = Field(name="IFEX_TP", column="AD")
    It1xTp = Field(name="IT1X_TP", column="Z")
    It2xTp = Field(name="IT2X_TP", column="AA")

    def to_omx(self) -> str:
        omx_block = (
            f'    <ct:object {self.Name.name}="{getattr(self, self.Name.key)}" base-type="{self.BASE_TYPE}" aspect="Aspects.PLC" access-level="public" uuid="{self.pk}">\n'
            f'      <attribute type="Attributes.{self.EUnit.name}" value="{getattr(self, self.EUnit.key)}"/>\n'
            f'      <attribute type="Attributes.FracDigits" value="2" />\n'
            f'      <attribute type="unit.System.Attributes.{self.Description.name}" value="{getattr(self, self.Description.key)}"/>\n'
            f'      <attribute type="Attributes.{self.IvxxTp.name}" value="{getattr(self, self.IvxxTp.key)}"/>\n'
            f'      <attribute type="Attributes.{self.Substance.name}" value="{getattr(self, self.Substance.key)}"/>\n'
            f'      <attribute type="Attributes.{self.GP.name}" value="{getattr(self, self.GP.key)}"/>\n'
            f'      <attribute type="Attributes.{self.IfexTp.name}" value="{getattr(self, self.IfexTp.key)}"/>\n'
            f'      <attribute type="Attributes.{self.It1xTp.name}" value="{getattr(self, self.It1xTp.key)}"/>\n'
            f'      <attribute type="Attributes.{self.It2xTp.name}" value="{getattr(self, self.It2xTp.key)}"/>\n'
            f"    </ct:object>\n"
        )
        return omx_block

    def to_hmi(self, x: int, y: int) -> str:
        hmi_block = (
            f'    <object access-modifier="private" name="{getattr(self, self.Name.key)}" display-name="{getattr(self, self.Name.key)}" uuid="{self.pk}" base-type="FB_QSA_S" base-type-id="624d8991-3d00-4518-96b0-0f5ff57827d6" ver="5" description="" cardinal="1">\n'
            f'        <designed target="X" value="{x}" ver="5"/>\n'
            f'        <designed target="Y" value="{y}" ver="5"/>\n'
            f'        <designed target="Rotation" value="0" ver="5"/>\n'
            f'        <init target="_init_Object" ver="5" value="KSPA001_SHU.{getattr(self, self.Name.key)}"/>\n'
            f"    </object>\n"
            f'    <object access-modifier="private" name="{getattr(self, self.Name.key)}" display-name="{getattr(self, self.Name.key)}" uuid="{self.tx}" base-type="Text" base-type-id="21d59f8d-2ca4-4592-92ca-b4dc48992a0f" ver="4">\n'
            f'        <designed target="X" value="{x+77}" ver="4"/>\n'
            f'        <designed target="Y" value="{y-75}" ver="4"/>\n'
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
