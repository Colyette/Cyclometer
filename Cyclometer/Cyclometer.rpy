I-Logix-RPY-Archive version 8.10.0 C++ 6930133
{ IProject 
	- _id = GUID 1cc64d65-8bc4-44ae-8edf-12aad3279c7a;
	- _myState = 8192;
	- _name = "Cyclometer";
	- _modifiedTimeWeak = 5.6.2015::18:12:32;
	- _lastID = 2;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Default.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Default";
		- _id = GUID 7917a40b-5dd4-4b9f-bbc7-887ed9a9d3f2;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "DefaultComponent.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "DefaultComponent";
		- _id = GUID 4beea14e-bbde-411c-acdb-3399ce533248;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 4;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ ISubsystem 
			- fileName = "Default";
			- _id = GUID 7917a40b-5dd4-4b9f-bbc7-887ed9a9d3f2;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 05e74a7c-de27-423a-a7ea-cf97c7b368de;
			- _myState = 8192;
			- _name = "Model1";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "4.23.2015::20:11:36";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 43360c87-61ae-4cf9-b2b0-5bdd7df0e735;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 05e74a7c-de27-423a-a7ea-cf97c7b368de;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 1;
				{ CGIClass 
					- _id = GUID 5b211b60-c0b5-4056-a084-6a726fd3c923;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 3194d975-ad33-4636-9d31-c61a2c993db1;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID ca5af121-f7fb-4ccd-99f1-73e87e06c09a;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID b0fa019e-41a7-43ae-b15f-7c40ae68b78b;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 5b211b60-c0b5-4056-a084-6a726fd3c923;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 7917a40b-5dd4-4b9f-bbc7-887ed9a9d3f2;
			}
		}
	}
	- MSCS = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IMSC 
			- _id = GUID 552307c8-5e7d-448c-88e3-757a9f2d40c0;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 12;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Condition_Mark";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,67,39";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "DataFlow";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "2";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Ellipse";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "FreeText";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "HorzAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Multiline";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "VertAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Wordbreak";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Polyline";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "TimeoutMessage";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "AutoNoCalcBikeStop";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "5.6.2015::18:12:42";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
				- m_usingActivationBar = 0;
				- _id = GUID 9dc719c7-d7c1-4bb9-844e-f134b4238ff5;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 552307c8-5e7d-448c-88e3-757a9f2d40c0;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 31;
				{ CGIBox 
					- _id = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID b1eb0b1a-1ab9-4137-bef6-20ef1b00ab2f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID c69a768b-a056-44b0-86b1-692297c28fab;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID c7317f70-38c9-4486-b2e6-51e367a796a9;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 2.14754 0 0 1 -447.262 54 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 361 291  544 291  544 623  361 623  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=332>
<frame Id=GUID ac962c23-8291-4614-a269-823c0302d34c>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID ac962c23-8291-4614-a269-823c0302d34c;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID dd657a5d-c241-4d98-9473-0ce38c620e74;
					}
					- m_pParent = GUID c69a768b-a056-44b0-86b1-692297c28fab;
					- m_name = { CGIText 
						- m_str = "pCnt=0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 361 291  544 291  544 623  361 623  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 43208a8f-b57c-4907-bc64-097ced953f08;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID c3ca4d8a-31d9-46b2-a148-63fef864f228;
					}
					- m_pParent = GUID ac962c23-8291-4614-a269-823c0302d34c;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.465649 0 0 1 209.198 -46 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 336 487  707 487  707 654  336 654  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=167>
<frame Id=GUID 61e4d330-b861-4651-ac22-d50d57356d5f>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID 2620ecbd-3907-4cf9-b8c7-6572581e20bb;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID c2d00eb9-eaa3-434e-b419-527a6620b13c;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "Mag";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0146136 50 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 577415d0-fe84-44ac-8f90-acf5d9cce5b4;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d8426f12-7363-419e-8427-ff0ab3716e77;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "PulseCounter";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0146136 208 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "Calculations";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0146136 337 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID b047c0df-485a-4c43-abec-2e578cd4a591;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID b8db4e7d-bd9c-4b33-b5ca-12724e886775;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "Trip";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0146136 494 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID b42d369e-3825-4a88-a726-859de86fbb88;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID ca19ed88-4582-4db3-835e-2fdb1cf59539;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "Display";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0146136 782 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscMessage 
					- _id = GUID c01dd3a2-4065-4666-9aa3-a94a5746171b;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 58d93566-ca1b-496e-bd97-6f8bf797d757;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "readPulseCounter()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -21 -8  86 -8  86 6  -21 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 267 ;
						- m_nHorizontalSpacing = -7;
						- m_nVerticalSpacing = -12;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_sourceType = 'F';
					- m_pTarget = GUID 577415d0-fe84-44ac-8f90-acf5d9cce5b4;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 18681 ;
					- m_TargetPort = 48 18681 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 2e245a91-bb1c-49c7-8d4f-5b73e5db8c7e;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c2ec76f7-3f1b-4a64-9847-7d890d74d368;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 577415d0-fe84-44ac-8f90-acf5d9cce5b4;
					- m_sourceType = 'F';
					- m_pTarget = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 19639 ;
					- m_TargetPort = 48 19639 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID b0c9bf3d-0857-4d9c-9f69-36cc9e55dbdf;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d5848f6b-4fe7-4a68-9ca7-38e6afd3ba12;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "clearWheelRot()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  84 -9  84 5  -6 5  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 393 352 ;
						- m_nHorizontalSpacing = 2;
						- m_nVerticalSpacing = 1;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_sourceType = 'F';
					- m_pTarget = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 415 356  415 376  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 20939 ;
					- m_TargetPort = 48 22308 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 6e083f7c-919a-4edb-ad82-8fb30d677750;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 33f05482-977f-4429-b536-2d505dcea8ee;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Tm(0.83s)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_sourceType = 'F';
					- m_pTarget = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 415 183  415 224  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 9101 ;
					- m_TargetPort = 48 11907 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 291c239e-cd4e-4cd5-973b-fbb01fa5f6ab;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7f031fb2-aac4-4244-9e46-52f82c0835e7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "calcUpdate()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_sourceType = 'F';
					- m_pTarget = GUID b42d369e-3825-4a88-a726-859de86fbb88;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 35994 ;
					- m_TargetPort = 48 35994 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 3ddc7c14-9085-4e32-a8d8-c0b97d26a7d8;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d119e345-6da7-435f-97dd-241370223bc8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "refreshScreen()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b42d369e-3825-4a88-a726-859de86fbb88;
					- m_sourceType = 'F';
					- m_pTarget = GUID b42d369e-3825-4a88-a726-859de86fbb88;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 860 596  860 616  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 37362 ;
					- m_TargetPort = 48 38731 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 71901638-8f93-4d28-9266-291fe3ea5d76;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3b7e15e1-72c5-4021-bf96-5fefdd791049;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "turnOff(WHEEL_LED)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -17 -8  103 -8  103 6  -17 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 432 362 ;
						- m_nHorizontalSpacing = 30;
						- m_nVerticalSpacing = -6;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_sourceType = 'F';
					- m_pTarget = GUID daad44d2-f374-4f54-b2f8-dec0c67d0189;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 413 396  413 416  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 23677 ;
					- m_TargetPort = 48 25045 ;
					- m_bLeft = 0;
				}
				{ CGIFreeShape 
					- _id = GUID b7c74327-c8ae-48f4-af54-1c0267c6bdf0;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.42254 0 0 1.125 -241.028 -19.875 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 516 119  587 119  587 159  516 159  ;
				}
				{ CGIFreeText 
					- _id = GUID 4a029950-1d28-4949-8144-b8778f3acf62;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -25 3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 518 123  620 123  620 141  518 141  ;
					- m_text = "TRIP_CALC_ON";
				}
				{ CGIFreeShape 
					- _id = GUID 7c0e08d5-8070-46c9-9456-4abcea790e8d;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -184 -99.963 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID 3159168a-a27d-4112-ae21-eb094bd93e14;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -15 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  399 124  399 142  361 142  ;
					- m_text = "ACCUM_WAIT";
				}
				{ CGIFreeShape 
					- _id = GUID c7a008e2-42ec-4007-801d-48a39cd615b9;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -188 27.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID 0e243554-2e9d-4530-9e00-b17a9a06ddd8;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -18 130 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  466 124  466 142  361 142  ;
					- m_text = "DET_MOTION";
				}
				{ CGIFreeShape 
					- _id = GUID 3c3197ff-9a8d-4e05-9d03-ab2c71cd4ddf;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -185 391.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID b7064eff-e608-42d0-8d6d-f8f41d0e1bd2;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -16 491 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  399 124  399 142  361 142  ;
					- m_text = "ACCUM_WAIT";
				}
				{ CGIFreeShape 
					- _id = GUID c5ce7073-d75c-46eb-88ba-a427cf57a8c6;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.42254 0 0 1.125 44.972 -17.875 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 516 119  587 119  587 159  516 159  ;
				}
				{ CGIFreeText 
					- _id = GUID b1fbdc2d-bf5c-4b9c-80d7-dd00376d7326;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 261 5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 518 123  630 123  630 141  518 141  ;
					- m_text = "SPEED_DISPLAY";
				}
				{ CGIAnnotation 
					- _id = GUID 6589bb35-40e4-4810-82e4-8efe1ecfd1b9;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "comment_11";
						- _id = GUID 2030ae43-3951-4bb2-ba9f-49110b16f0c6;
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.0590406 0 0 0.103291 25 108.69 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1097  1084 1097  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIFreeText 
					- _id = GUID 461d1358-87e0-44a8-9130-0023c537f715;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -143 148 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 597 164  676 164  676 182  597 182  ;
					- m_text = "AUTO:TRUE";
				}
				{ CGIFreeShape 
					- _id = GUID 85d251e8-3e58-492f-a948-3b88ebb5719f;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -188 235.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID 1b236eed-8046-44ac-90ba-1babb3d0e73f;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -24 338 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  469 124  469 142  361 142  ;
					- m_text = "DET_TRIP_CALC";
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 61e4d330-b861-4651-ac22-d50d57356d5f;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 88626756-96ee-4de4-a7f2-2ed8baa68cba;
					}
					- m_pParent = GUID 43208a8f-b57c-4907-bc64-097ced953f08;
					- m_name = { CGIText 
						- m_str = "AUTO";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 336 487  707 487  707 654  336 654  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 40860b4c-d6c0-456a-8ec7-0012d16be804;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 7917a40b-5dd4-4b9f-bbc7-887ed9a9d3f2;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID b1eb0b1a-1ab9-4137-bef6-20ef1b00ab2f;
				- _modifiedTimeWeak = 1.2.1990::0:0:0;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IClassifierRole 
						- _id = GUID c2d00eb9-eaa3-434e-b419-527a6620b13c;
						- _name = "Mag";
						- _modifiedTimeWeak = 5.6.2015::17:7:13;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID d8426f12-7363-419e-8427-ff0ab3716e77;
						- _name = "PulseCounter";
						- _modifiedTimeWeak = 5.6.2015::17:7:13;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						- _name = "Calculations";
						- _modifiedTimeWeak = 5.6.2015::17:7:13;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID b8db4e7d-bd9c-4b33-b5ca-12724e886775;
						- _name = "Trip";
						- _modifiedTimeWeak = 5.6.2015::17:7:13;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID ca19ed88-4582-4db3-835e-2fdb1cf59539;
						- _name = "Display";
						- _modifiedTimeWeak = 5.6.2015::17:7:13;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 7;
					- value = 
					{ IMessage 
						- _id = GUID 33f05482-977f-4429-b536-2d505dcea8ee;
						- _myState = 8192;
						- _name = "Tm";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "1.";
						- m_szActualArgs = "0.83s";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 58d93566-ca1b-496e-bd97-6f8bf797d757;
						- _name = "readPulseCounter";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8426f12-7363-419e-8427-ff0ab3716e77;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID c2ec76f7-3f1b-4a64-9847-7d890d74d368;
						- _myState = 2048;
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "3.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d8426f12-7363-419e-8427-ff0ab3716e77;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d5848f6b-4fe7-4a68-9ca7-38e6afd3ba12;
						- _myState = 8192;
						- _name = "clearWheelRot";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 7f031fb2-aac4-4244-9e46-52f82c0835e7;
						- _name = "calcUpdate";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ca19ed88-4582-4db3-835e-2fdb1cf59539;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID d119e345-6da7-435f-97dd-241370223bc8;
						- _myState = 8192;
						- _name = "refreshScreen";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "7.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ca19ed88-4582-4db3-835e-2fdb1cf59539;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID ca19ed88-4582-4db3-835e-2fdb1cf59539;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 3b7e15e1-72c5-4021-bf96-5fefdd791049;
						- _myState = 8192;
						- _name = "turnOff";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "5.";
						- m_szActualArgs = "WHEEL_LED";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- InteractionOccurrences = { IRPYRawContainer 
					- size = 0;
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ ICombinedFragment 
						- _id = GUID c7317f70-38c9-4486-b2e6-51e367a796a9;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID dd657a5d-c241-4d98-9473-0ce38c620e74;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _modifiedTimeWeak = 5.6.2015::18:10:47;
								- CombinedFragments = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ ICombinedFragment 
										- _id = GUID c3ca4d8a-31d9-46b2-a148-63fef864f228;
										- _myState = 2048;
										- _name = "interactionOperator_1";
										- _modifiedTimeWeak = 1.2.1990::0:0:0;
										- _interactionOperator = "opt";
										- InteractionOperands = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IInteractionOperand 
												- _id = GUID 88626756-96ee-4de4-a7f2-2ed8baa68cba;
												- _myState = 2048;
												- _name = "interactionOperand_0";
												- _modifiedTimeWeak = 5.6.2015::18:10:47;
												- _interactionConstraint = "AUTO";
											}
										}
									}
								}
								- _interactionConstraint = "pCnt=0";
							}
						}
					}
				}
			}
		}
		{ IMSC 
			- _id = GUID 36714bef-8a65-4e9f-a263-98c0bfa980be;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 10;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "CombinedFragment";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,250,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Comment";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,116,60";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "194,192,192";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Ellipse";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "FreeText";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "HorzAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Multiline";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "VertAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Wordbreak";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InstanceLine";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,96,437";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "InteractionOperand";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,150";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Message";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Polyline";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "ReplyMessage";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "TimeoutMessage";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "SpeedCalc";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "5.6.2015::18:6:40";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 6;
				- m_usingActivationBar = 0;
				- _id = GUID 353e6925-5b8e-4e5c-b442-46bf2647c8b9;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IMSC";
					- _id = GUID 36714bef-8a65-4e9f-a263-98c0bfa980be;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 42;
				{ CGIBox 
					- _id = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_type = 108;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICollaboration";
						- _id = GUID 9c85c456-2b32-4652-846b-e937832697c6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID ac53983e-46c8-404d-a315-047b1e94b4a2;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID 1cc44a4f-40e2-43e8-83f9-93bee3497fd0;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "interactionOperator_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 2.14754 0 0 1 -452.262 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_bFramesetModified = 1;
					- m_polygon = 4 361 291  544 291  544 1040  361 1040  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=749>
<frame Id=GUID 14ae4a74-68e4-472f-9e5b-97cb39f89fa1>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 14ae4a74-68e4-472f-9e5b-97cb39f89fa1;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID afb9da12-4ad0-42ec-a462-4c28da56766f;
					}
					- m_pParent = GUID ac53983e-46c8-404d-a315-047b1e94b4a2;
					- m_name = { CGIText 
						- m_str = "pCnt >0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 361 291  544 291  544 1040  361 1040  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID f82aa7e7-076d-4b3a-8956-2962fd8cc444;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID ef420db4-7ba9-46e0-bef5-1af261dd8652;
					}
					- m_pParent = GUID 14ae4a74-68e4-472f-9e5b-97cb39f89fa1;
					- m_name = { CGIText 
						- m_str = "interactionOperator_1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.66578 0 0 1 115.376 -124 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 376 718  611 718  611 1005  376 1005  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=287>
<frame Id=GUID 264ec5bd-abed-4f89-b6e9-e2bb2bc89c1c>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 264ec5bd-abed-4f89-b6e9-e2bb2bc89c1c;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID f338330e-93e7-4c31-95b0-ac5f0c98d328;
					}
					- m_pParent = GUID f82aa7e7-076d-4b3a-8956-2962fd8cc444;
					- m_name = { CGIText 
						- m_str = "AUTO";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nHorizontalSpacing = 5;
						- m_nVerticalSpacing = 3;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 376 718  611 718  611 1005  376 1005  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscColumnCR 
					- _id = GUID cc145743-e226-4e12-be2a-986643fe6113;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e72c649c-7acc-4215-85d9-e31c61312c73;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "Mag";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0242157 45 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID ac06c9d9-b014-4898-a835-4641025b08ba;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID e25e8e7e-3a1a-4046-b329-54277e7ca3a1;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "PulseCounter";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0242157 203 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "Calculations";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0242157 332 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 10773deb-ef50-46e5-aa19-d27398f15c0b;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID bde0f412-34de-411b-bda1-9ffe8d245591;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "Trip";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0242157 489 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscColumnCR 
					- _id = GUID 2ccf5f54-3c0f-4710-808e-c90f62ba54da;
					- m_type = 109;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClassifierRole";
						- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "Display";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_transform = 1 0 0 0.0242157 777 50 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_position = 4 0 0  0 49885  96 49885  96 0  ;
					- m_pInheritsFrom = { IHandle 
						- _m2Class = "";
					}
					- m_nInheritanceMask = 0;
					- m_SubType = 0;
				}
				{ CGIMscMessage 
					- _id = GUID e9b1a3eb-63f8-44ad-9a56-3af9813a41c1;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 75171fe8-efed-449b-bb88-cfeb24554225;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pulse()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cc145743-e226-4e12-be2a-986643fe6113;
					- m_sourceType = 'F';
					- m_pTarget = GUID ac06c9d9-b014-4898-a835-4641025b08ba;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 3221 ;
					- m_TargetPort = 48 3221 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID c5047773-e6ea-4df9-ada8-1d3f80f67162;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 5fc48934-fa1e-42e6-bd55-c4a87fd750a7;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "pulse()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cc145743-e226-4e12-be2a-986643fe6113;
					- m_sourceType = 'F';
					- m_pTarget = GUID ac06c9d9-b014-4898-a835-4641025b08ba;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 4666 ;
					- m_TargetPort = 48 4666 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 8c4cf5dd-8b9b-4ce8-82b7-02f39bc5b503;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 192fd29e-7f66-4cc0-aa3f-0c7a55e6a599;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "readPulseCounter()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -21 -8  86 -8  86 6  -21 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 267 ;
						- m_nHorizontalSpacing = -7;
						- m_nVerticalSpacing = -12;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID ac06c9d9-b014-4898-a835-4641025b08ba;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 11274 ;
					- m_TargetPort = 48 11274 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 7e61c585-8a8d-4630-8d50-1240b779948d;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID df3fbc5f-f25c-415a-b2da-020c1af24300;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID ac06c9d9-b014-4898-a835-4641025b08ba;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 11852 ;
					- m_TargetPort = 48 11852 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID f96eb290-6cc9-4c2c-aac9-c2834ba1af70;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 34a7c1d8-f164-4517-a3d4-55ab7abd7726;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "toggle(WHEEL_LED)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -1 -8  79 -8  79 6  -1 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 386 465 ;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 408 489  408 516  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 18129 ;
					- m_TargetPort = 48 19244 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID e19b3ac0-dbae-4352-a477-4cf420c8287a;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID e335866b-afc4-4617-a48b-9a4b216560f6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "setWheelRot()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -1 -8  79 -8  79 6  -1 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 386 465 ;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 410 444  410 469  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 16270 ;
					- m_TargetPort = 48 17303 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID a3182278-8030-4b20-b8bd-325846953012;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID a38280ad-6e18-4dd1-8916-e5060c1d3af4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "calcSpeed()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  62 -9  62 5  -6 5  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 390 529 ;
						- m_nHorizontalSpacing = 4;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 410 617  410 638  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 23415 ;
					- m_TargetPort = 48 24282 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 7bee4e2e-dd9b-41a5-ae53-1a17dd2b174e;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 3813719a-0350-4ebb-b0e4-3d5d65cf157f;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "calcAvgSpeed()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 1 -8  69 -8  69 6  1 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 388 565 ;
						- m_nHorizontalSpacing = 4;
						- m_nVerticalSpacing = -14;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 412 884  412 905  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 34441 ;
					- m_TargetPort = 48 35308 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 2cc73fe4-933e-4d85-80c1-6c82516d0829;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 7f3b4408-dba6-4a86-8ff9-6a3f0fe4c77d;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "calcDistance()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  73 -9  73 5  -6 5  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 401 633 ;
						- m_nHorizontalSpacing = 15;
						- m_nVerticalSpacing = -3;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 410 844  410 872  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 32789 ;
					- m_TargetPort = 48 33945 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 68d65c0c-c0c4-41e3-b1a5-fbcd214120cf;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4e365f3a-ecd7-4cca-9ed8-5b48ee567e55;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Tm(0.83s)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 410 183  410 224  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 5492 ;
					- m_TargetPort = 48 7185 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 5a24324f-caf0-49b1-9d31-998eb5e534bc;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 63c68f89-a91b-49ea-aa29-bf967559de57;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "calcUpdate()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2ccf5f54-3c0f-4710-808e-c90f62ba54da;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 35803 ;
					- m_TargetPort = 48 35803 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 1935520c-162b-468b-9b70-8f7067e16fb0;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 9d1dde9e-1bc9-4941-994a-b2112213e2e4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "refreshScreen()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  81 -9  81 5  -6 5  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 829 768 ;
						- m_nHorizontalSpacing = -2;
						- m_nVerticalSpacing = 4;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2ccf5f54-3c0f-4710-808e-c90f62ba54da;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2ccf5f54-3c0f-4710-808e-c90f62ba54da;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 859 923  859 955  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 36051 ;
					- m_TargetPort = 48 37373 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID edd23435-c8ec-43f9-91ff-476d0828603e;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 41080c74-e5a5-49f7-b808-81b3e3eb619e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "clearPulseCounter()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -1 -8  79 -8  79 6  -1 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 386 465 ;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 408 382  408 409  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 13710 ;
					- m_TargetPort = 48 14825 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID aac2319b-cee7-4c14-8ea3-47753297f892;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 546b1b13-2e71-4b17-96b3-b8faffb52fb3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "getElapsedTime()";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 2ccf5f54-3c0f-4710-808e-c90f62ba54da;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 25851 ;
					- m_TargetPort = 48 25851 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 66045808-5611-4f5e-b78d-51d62f4d6a1d;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 24740c45-eff9-44af-b418-cd481e74d1a4;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "toggle(AUTO_LED)";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -1 -8  79 -8  79 6  -1 6  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 386 465 ;
						- m_nVerticalSpacing = -5;
						- m_nOrientationCtrlPt = 6;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_arrow = 2 408 723  408 742  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 27792 ;
					- m_TargetPort = 48 28577 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID c5c0b78d-cd74-4cbc-a1ce-f867af60fb8f;
					- m_type = 193;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 4e70ac13-ecd6-4788-bffb-0e0dcb257fdb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 2ccf5f54-3c0f-4710-808e-c90f62ba54da;
					- m_sourceType = 'F';
					- m_pTarget = GUID 4451aaa9-5271-42ba-adab-35bf92016b29;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 48 26388 ;
					- m_TargetPort = 48 26388 ;
					- m_bLeft = 0;
				}
				{ CGIFreeShape 
					- _id = GUID 672d3981-b5ce-4947-9d7c-5032ba006cf4;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.42254 0 0 1.125 -246.028 -19.875 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 516 119  587 119  587 159  516 159  ;
				}
				{ CGIFreeText 
					- _id = GUID a5a848b8-9b33-4a6f-a1d2-3bc137ce55f4;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -30 3 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 518 123  620 123  620 141  518 141  ;
					- m_text = "TRIP_CALC_ON";
				}
				{ CGIFreeShape 
					- _id = GUID 908182e9-9438-4a29-b54a-60311c206390;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -189 -99.963 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID f74f3fa0-b509-42ec-bbda-3d9373109dbd;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -20 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  399 124  399 142  361 142  ;
					- m_text = "ACCUM_WAIT";
				}
				{ CGIFreeShape 
					- _id = GUID 25e77ad5-7769-4202-91e9-cbdad6b3e86b;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -193 27.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID 76fb749d-038c-4be6-b8b5-7466570381a5;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -23 130 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  466 124  466 142  361 142  ;
					- m_text = "DET_MOTION";
				}
				{ CGIFreeShape 
					- _id = GUID 9ddf6511-abae-424b-9329-cb4097f06e4e;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.47887 0 0 1.7037 -193 335.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID 73f8b598-c8b5-478b-b506-d4a52a5723f4;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -24 438 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  466 124  466 142  361 142  ;
					- m_text = "SPEED_UPDATE";
				}
				{ CGIFreeShape 
					- _id = GUID 31252c60-6fc8-4f28-a3be-96b5a920d4aa;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 2.07042 0 0 1.7037 -391 583.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID 96f78748-cd30-4335-93f7-9e0d6d19b253;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -10 684 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  477 124  477 142  361 142  ;
					- m_text = "TRIP_CALC_UPDATE";
				}
				{ CGIFreeShape 
					- _id = GUID 98680468-17dd-4cc7-a78b-4a3d0647016e;
					- m_type = 188;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.42254 0 0 1.125 39.972 -17.875 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 516 119  587 119  587 159  516 159  ;
				}
				{ CGIFreeText 
					- _id = GUID 807e62c0-fff7-4ebc-a526-a27514ca114d;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 256 5 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 518 123  630 123  630 141  518 141  ;
					- m_text = "SPEED_DISPLAY";
				}
				{ CGIFreeShape 
					- _id = GUID 80a8358d-8d01-4f76-9d71-c3e643a50c4d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Polyline";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Line.LineStyle";
												- _Value = "2";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 183;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -4 -6 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 2 119 133  119 169  ;
				}
				{ CGIAnnotation 
					- _id = GUID 561e0f27-7a93-49b3-968e-79d3e7bb4187;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 173;
					- m_pModelObject = { IHandle 
						- _m2Class = "IComment";
						- _filename = "Default.sbs";
						- _subsystem = "Default";
						- _class = "";
						- _name = "comment_11";
						- _id = GUID 2030ae43-3951-4bb2-ba9f-49110b16f0c6;
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.0590406 0 0 0.103291 20 108.69 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 3  0 1097  1084 1097  1084 3  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- _iTempdisplayTextFlag = 2;
					- m_bIsBoxStyle = 0;
				}
				{ CGIFreeText 
					- _id = GUID f47f3755-85df-475b-ac8c-18fee30f76fa;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -5 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 150 114  188 114  188 132  150 132  ;
					- m_text = "1";
				}
				{ CGIFreeText 
					- _id = GUID 5aa198bf-1126-4a13-bc60-3a63afa9c2f2;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -5 0 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 135 144  173 144  173 162  135 162  ;
					- m_text = "n";
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 68c9645e-f0b1-4c0c-9b34-eaf6bdc446b1;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Default.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Default";
				- _id = GUID 7917a40b-5dd4-4b9f-bbc7-887ed9a9d3f2;
			}
			- m_pICollaboration = { ICollaboration 
				- _id = GUID 9c85c456-2b32-4652-846b-e937832697c6;
				- _modifiedTimeWeak = 1.2.1990::0:0:0;
				- ClassifierRoles = { IRPYRawContainer 
					- size = 5;
					- value = 
					{ IClassifierRole 
						- _id = GUID e72c649c-7acc-4215-85d9-e31c61312c73;
						- _name = "Mag";
						- _modifiedTimeWeak = 5.4.2015::18:4:1;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID e25e8e7e-3a1a-4046-b329-54277e7ca3a1;
						- _name = "PulseCounter";
						- _modifiedTimeWeak = 5.4.2015::18:4:40;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						- _name = "Calculations";
						- _modifiedTimeWeak = 5.4.2015::18:5:6;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID bde0f412-34de-411b-bda1-9ffe8d245591;
						- _name = "Trip";
						- _modifiedTimeWeak = 5.4.2015::18:5:24;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
					{ IClassifierRole 
						- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
						- _name = "Display";
						- _modifiedTimeWeak = 5.5.2015::19:11:7;
						- m_eRoleType = CLASS;
						- m_pBase = { IHandle 
							- _m2Class = "";
						}
						- m_instance = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- Messages = { IRPYRawContainer 
					- size = 16;
					- value = 
					{ IMessage 
						- _id = GUID 75171fe8-efed-449b-bb88-cfeb24554225;
						- _name = "pulse";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "1.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e25e8e7e-3a1a-4046-b329-54277e7ca3a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e72c649c-7acc-4215-85d9-e31c61312c73;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 5fc48934-fa1e-42e6-bd55-c4a87fd750a7;
						- _name = "pulse";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "2.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e25e8e7e-3a1a-4046-b329-54277e7ca3a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e72c649c-7acc-4215-85d9-e31c61312c73;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 192fd29e-7f66-4cc0-aa3f-0c7a55e6a599;
						- _name = "readPulseCounter";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "4.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e25e8e7e-3a1a-4046-b329-54277e7ca3a1;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID df3fbc5f-f25c-415a-b2da-020c1af24300;
						- _myState = 2048;
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "5.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID e25e8e7e-3a1a-4046-b329-54277e7ca3a1;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 34a7c1d8-f164-4517-a3d4-55ab7abd7726;
						- _myState = 8192;
						- _name = "toggle";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "8.";
						- m_szActualArgs = "WHEEL_LED";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID e335866b-afc4-4617-a48b-9a4b216560f6;
						- _myState = 8192;
						- _name = "setWheelRot";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "7.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID a38280ad-6e18-4dd1-8916-e5060c1d3af4;
						- _myState = 8192;
						- _name = "calcSpeed";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "9.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 3813719a-0350-4ebb-b0e4-3d5d65cf157f;
						- _myState = 8192;
						- _name = "calcAvgSpeed";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "14.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 7f3b4408-dba6-4a86-8ff9-6a3f0fe4c77d;
						- _myState = 8192;
						- _name = "calcDistance";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "13.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4e365f3a-ecd7-4cca-9ed8-5b48ee567e55;
						- _myState = 8192;
						- _name = "Tm";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "3.";
						- m_szActualArgs = "0.83s";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 63c68f89-a91b-49ea-aa29-bf967559de57;
						- _name = "calcUpdate";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "15.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = EVENT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 9d1dde9e-1bc9-4941-994a-b2112213e2e4;
						- _myState = 8192;
						- _name = "refreshScreen";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "16.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 41080c74-e5a5-49f7-b808-81b3e3eb619e;
						- _myState = 8192;
						- _name = "clearPulseCounter";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "6.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 546b1b13-2e71-4b17-96b3-b8faffb52fb3;
						- _name = "getElapsedTime";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "10.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = PRIMITIVE;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 24740c45-eff9-44af-b418-cd481e74d1a4;
						- _myState = 8192;
						- _name = "toggle";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "12.";
						- m_szActualArgs = "AUTO_LED";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = TIMEOUT;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
					{ IMessage 
						- _id = GUID 4e70ac13-ecd6-4788-bffb-0e0dcb257fdb;
						- _myState = 2048;
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "11.";
						- m_szActualArgs = "";
						- m_szReturnVal = "";
						- m_pCommunicationConnection = { IHandle 
							- _m2Class = "";
						}
						- m_pReceiver = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID 66b236fc-0fcf-49ff-80d5-c17bc4e4f39e;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID d3d6e688-6c32-46cd-a7d3-950f8bf5e830;
						}
						- m_pFormalMessage = { IHandle 
							- _m2Class = "";
						}
						- m_eType = REPLY;
						- m_targetExec = { IHandle 
							- _m2Class = "";
						}
						- m_srcExec = { IHandle 
							- _m2Class = "";
						}
					}
				}
				- CombinedFragments = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ ICombinedFragment 
						- _id = GUID 1cc44a4f-40e2-43e8-83f9-93bee3497fd0;
						- _myState = 2048;
						- _name = "interactionOperator_0";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- _interactionOperator = "opt";
						- InteractionOperands = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IInteractionOperand 
								- _id = GUID afb9da12-4ad0-42ec-a462-4c28da56766f;
								- _myState = 2048;
								- _name = "interactionOperand_1";
								- _modifiedTimeWeak = 5.6.2015::17:59:40;
								- CombinedFragments = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ ICombinedFragment 
										- _id = GUID ef420db4-7ba9-46e0-bef5-1af261dd8652;
										- _myState = 2048;
										- _name = "interactionOperator_1";
										- _modifiedTimeWeak = 1.2.1990::0:0:0;
										- _interactionOperator = "opt";
										- InteractionOperands = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IInteractionOperand 
												- _id = GUID f338330e-93e7-4c31-95b0-ac5f0c98d328;
												- _myState = 2048;
												- _name = "interactionOperand_0";
												- _modifiedTimeWeak = 5.6.2015::17:59:40;
												- _interactionConstraint = "AUTO";
											}
										}
									}
								}
								- _interactionConstraint = "pCnt >0";
							}
						}
					}
				}
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "DefaultComponent";
			- _id = GUID 4beea14e-bbde-411c-acdb-3399ce533248;
		}
	}
}

