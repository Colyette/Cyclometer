I-Logix-RPY-Archive version 8.10.0 C++ 6930133
{ IProject 
	- _id = GUID 1cc64d65-8bc4-44ae-8edf-12aad3279c7a;
	- _myState = 8192;
	- _name = "Cyclometer";
	- _modifiedTimeWeak = 5.4.2015::18:46:36;
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
			- _lastModifiedTime = "5.4.2015::18:46:37";
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
					- m_polygon = 4 361 269  544 269  544 775  361 775  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=117,389>
<frame Id=GUID ac962c23-8291-4614-a269-823c0302d34c>
<frame Id=GUID a9bab170-269d-48c4-b99f-30bb267eec60>";
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperand 
					- _id = GUID a9bab170-269d-48c4-b99f-30bb267eec60;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID d98741b4-8029-450c-9daf-3bdd53d8c47e;
					}
					- m_pParent = GUID c69a768b-a056-44b0-86b1-692297c28fab;
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
					- m_polygon = 4 361 386  544 386  544 775  361 775  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
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
					- m_polygon = 4 361 269  544 269  544 386  361 386  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIMscInteractionOperator 
					- m_operatorType = "opt";
					- _id = GUID 911e2503-7017-4be8-8c4a-203682bca9b8;
					- m_type = 196;
					- m_pModelObject = { IHandle 
						- _m2Class = "ICombinedFragment";
						- _id = GUID cb1ecb71-9a1a-459e-a25a-b41830518bef;
					}
					- m_pParent = GUID a9bab170-269d-48c4-b99f-30bb267eec60;
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
					- m_transform = 0.66578 0 0 1 115.376 -75 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 376 639  611 639  611 830  376 830  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=191>
<frame Id=GUID 6989d485-ff15-4874-bcfe-84136e465639>";
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
					- m_transform = 1 0 0 0.0187231 50 50 ;
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
					- m_transform = 1 0 0 0.0187231 208 50 ;
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
					- m_transform = 1 0 0 0.0187231 337 50 ;
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
					- m_transform = 1 0 0 0.0187231 494 50 ;
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
					- _id = GUID 6e083f7c-919a-4edb-ad82-8fb30d677750;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 33f05482-977f-4429-b536-2d505dcea8ee;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Tm(poll_rate)";
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
					- m_arrow = 2 415 173  415 202  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 6569 ;
					- m_TargetPort = 48 8118 ;
					- m_bLeft = 0;
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
					- m_SourcePort = 48 13406 ;
					- m_TargetPort = 48 13406 ;
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
					- m_SourcePort = 48 14154 ;
					- m_TargetPort = 48 14154 ;
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
					- m_arrow = 2 415 343  415 374  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 15649 ;
					- m_TargetPort = 48 17305 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID e0676f29-201b-448d-9b8a-2edeeba5f38f;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID 810dd8fb-97b6-4532-b251-bd6f6ec221ca;
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
					- m_arrow = 2 415 460  415 492  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 21898 ;
					- m_TargetPort = 48 23607 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID bb4ed5a7-8d19-4420-b4f3-0ef7f0762c90;
					- m_type = 110;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID d00620c1-edfb-4daa-b577-816f3569d158;
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
					- m_pSource = GUID 2620ecbd-3907-4cf9-b8c7-6572581e20bb;
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
					- m_SourcePort = 48 4166 ;
					- m_TargetPort = 48 4166 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 39b007f4-aa82-4faa-beb2-98be7c6fae00;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID c9b1da87-80e8-4c68-bcaa-ab4dc959ca56;
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
					- m_arrow = 2 415 576  415 597  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 28094 ;
					- m_TargetPort = 48 29215 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID 9fdffc7a-eb04-4345-a4d5-e41fc75ebb9d;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID f1b91ff0-4cf6-45cc-96df-dfee5c2f832c;
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
					- m_arrow = 2 415 719  415 740  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 35731 ;
					- m_TargetPort = 48 36853 ;
					- m_bLeft = 0;
				}
				{ CGIMscMessage 
					- _id = GUID dbc85c8c-27f3-4f2c-819a-940a694919f7;
					- m_type = 115;
					- m_pModelObject = { IHandle 
						- _m2Class = "IMessage";
						- _id = GUID ca3ab423-901c-493d-8113-72db380761ed;
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
						- m_position = 4 -9 -7  70 -7  70 7  -9 7  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 398 752 ;
						- m_nHorizontalSpacing = 4;
						- m_nVerticalSpacing = -9;
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
					- m_arrow = 2 415 768  415 789  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 48 38348 ;
					- m_TargetPort = 48 39470 ;
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
					- m_transform = 1.47887 0 0 1.7037 -188 5.037 ;
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
					- m_transform = 1 0 0 1 -18 108 ;
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
					- m_transform = 1.47887 0 0 1.7037 -186 176.037 ;
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
					- m_transform = 1 0 0 1 -17 276 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  399 124  399 142  361 142  ;
					- m_text = "ACCUM_WAIT";
				}
				{ CGIFreeShape 
					- _id = GUID 569ce423-c358-465e-b9b1-50e4e5e7bab6;
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
					- m_transform = 1.47887 0 0 1.7037 -188 294.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID dcc31075-41ad-4a4d-ab57-68734783264b;
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
					- m_transform = 1 0 0 1 -19 394 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  466 124  466 142  361 142  ;
					- m_text = "SPEED_UPDATE";
				}
				{ CGIMscInteractionOperand 
					- _id = GUID 6989d485-ff15-4874-bcfe-84136e465639;
					- m_type = 197;
					- m_pModelObject = { IHandle 
						- _m2Class = "IInteractionOperand";
						- _id = GUID 5e598f11-f7bc-4910-899b-9966f6585953;
					}
					- m_pParent = GUID 911e2503-7017-4be8-8c4a-203682bca9b8;
					- m_name = { CGIText 
						- m_str = "TCalcFlg";
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
					- m_polygon = 4 376 639  611 639  611 830  376 830  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIFreeShape 
					- _id = GUID d425673f-4798-45f6-a998-e29dac3255fb;
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
					- m_transform = 2.07042 0 0 1.7037 -396 433.037 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 355 125  426 125  426 152  355 152  ;
				}
				{ CGIFreeText 
					- _id = GUID e171f3b2-3638-4be3-8b53-bf69accf9c9d;
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
					- m_transform = 1 0 0 1 -16 537 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 361 124  477 124  477 142  361 142  ;
					- m_text = "TRIP_CALC_UPDATE";
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
					- size = 4;
					- value = 
					{ IClassifierRole 
						- _id = GUID c2d00eb9-eaa3-434e-b419-527a6620b13c;
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
						- _id = GUID d8426f12-7363-419e-8427-ff0ab3716e77;
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
						- _id = GUID bd1ea711-df9c-463f-8b39-c4ba0de6b8b4;
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
						- _id = GUID b8db4e7d-bd9c-4b33-b5ca-12724e886775;
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
				}
				- Messages = { IRPYRawContainer 
					- size = 9;
					- value = 
					{ IMessage 
						- _id = GUID 33f05482-977f-4429-b536-2d505dcea8ee;
						- _myState = 8192;
						- _name = "Tm";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "2.";
						- m_szActualArgs = "poll_rate";
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
						- m_szSequence = "3.";
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
						- m_szSequence = "5.";
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
						- _id = GUID 810dd8fb-97b6-4532-b251-bd6f6ec221ca;
						- _myState = 8192;
						- _name = "setWheelRot";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "6.";
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
						- _id = GUID d00620c1-edfb-4daa-b577-816f3569d158;
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
							- _id = GUID d8426f12-7363-419e-8427-ff0ab3716e77;
						}
						- m_pSender = { IHandle 
							- _m2Class = "IClassifierRole";
							- _id = GUID c2d00eb9-eaa3-434e-b419-527a6620b13c;
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
						- _id = GUID c9b1da87-80e8-4c68-bcaa-ab4dc959ca56;
						- _myState = 8192;
						- _name = "calcSpeed";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "7.";
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
						- _id = GUID f1b91ff0-4cf6-45cc-96df-dfee5c2f832c;
						- _myState = 8192;
						- _name = "calcAvgSpeed";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "8.";
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
						- _id = GUID ca3ab423-901c-493d-8113-72db380761ed;
						- _myState = 8192;
						- _name = "calcDistance";
						- _modifiedTimeWeak = 1.2.1990::0:0:0;
						- m_szSequence = "9.";
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
							- size = 2;
							- value = 
							{ IInteractionOperand 
								- _id = GUID dd657a5d-c241-4d98-9473-0ce38c620e74;
								- _myState = 2048;
								- _name = "interactionOperand_0";
								- _modifiedTimeWeak = 5.4.2015::18:14:2;
								- _interactionConstraint = "pCnt=0";
							}
							{ IInteractionOperand 
								- _id = GUID d98741b4-8029-450c-9daf-3bdd53d8c47e;
								- _myState = 2048;
								- _name = "interactionOperand_1";
								- _modifiedTimeWeak = 5.4.2015::18:43:34;
								- CombinedFragments = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ ICombinedFragment 
										- _id = GUID cb1ecb71-9a1a-459e-a25a-b41830518bef;
										- _myState = 2048;
										- _name = "interactionOperator_1";
										- _modifiedTimeWeak = 1.2.1990::0:0:0;
										- _interactionOperator = "opt";
										- InteractionOperands = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IInteractionOperand 
												- _id = GUID 5e598f11-f7bc-4910-899b-9966f6585953;
												- _myState = 2048;
												- _name = "interactionOperand_0";
												- _modifiedTimeWeak = 5.4.2015::18:44:2;
												- _interactionConstraint = "TCalcFlg";
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
		{ IMSC 
			- _id = GUID 36714bef-8a65-4e9f-a263-98c0bfa980be;
			- _myState = 8192;
			- _name = "SpeedCalc";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "5.4.2015::17:43:42";
			- _graphicChart = { CGIMscChart 
				- vLadderMargin = 20;
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
				- elementList = 1;
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

